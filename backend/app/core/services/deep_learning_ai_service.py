from typing import List, Dict, Any, Optional
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import AutoTokenizer, AutoModel
import numpy as np
from datetime import datetime
import json
import spacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import gym
from app.core.config import settings
from app.core.domain.entities import UserStory, Sprint, ProductBacklog, Feedback

class DeepLearningModel(nn.Module):
    """Derin öğrenme modeli"""
    
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        super(DeepLearningModel, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.layers(x)

class ProductOwnerEnvironment(gym.Env):
    """Product Owner için özel ortam"""
    
    def __init__(self):
        super(ProductOwnerEnvironment, self).__init__()
        self.action_space = gym.spaces.Discrete(10)  # 10 farklı aksiyon
        self.observation_space = gym.spaces.Box(
            low=-np.inf, high=np.inf, shape=(50,), dtype=np.float32
        )
        self.state = None
        self.reset()
    
    def reset(self):
        self.state = np.zeros(50)
        return self.state
    
    def step(self, action):
        # Aksiyonları uygula ve ödül hesapla
        reward = self._calculate_reward(action)
        self.state = self._update_state(action)
        done = False
        info = {}
        return self.state, reward, done, info
    
    def _calculate_reward(self, action):
        # Ödül hesaplama mantığı
        return 0.0
    
    def _update_state(self, action):
        # Durum güncelleme mantığı
        return self.state

class DeepLearningAIProductOwner:
    """Derin öğrenme yetenekleri ve güçlü agent ile donatılmış AI Product Owner"""

    def __init__(self):
        # Derin öğrenme modelleri
        self.story_analyzer = DeepLearningModel(768, 512, 256)
        self.velocity_predictor = DeepLearningModel(256, 128, 1)
        self.risk_analyzer = DeepLearningModel(512, 256, 128)
        
        # NLP modelleri
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
        self.bert_model = AutoModel.from_pretrained('bert-base-uncased')
        self.nlp = spacy.load('en_core_web_sm')
        nltk.download('punkt')
        nltk.download('stopwords')
        
        # Word2Vec modeli
        self.word2vec = Word2Vec(vector_size=100, window=5, min_count=1)
        
        # RL Agent
        self.env = DummyVecEnv([lambda: ProductOwnerEnvironment()])
        self.agent = PPO('MlpPolicy', self.env, verbose=1)
        
        # Öğrenme geçmişi
        self.learning_history = {
            "story_embeddings": [],
            "velocity_predictions": [],
            "risk_assessments": [],
            "agent_actions": [],
            "rewards": []
        }
        
        # Model eğitimi için optimizer
        self.optimizer = optim.Adam(self.story_analyzer.parameters())
        self.criterion = nn.MSELoss()

    async def analyze_user_story(self, story: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """User story'yi derin öğrenme ile analiz eder."""
        # Metin gömme
        story_embedding = self._get_story_embedding(story)
        
        # Derin öğrenme analizi
        story_features = self.story_analyzer(torch.FloatTensor(story_embedding))
        
        # Karmaşıklık analizi
        complexity = self._analyze_complexity(story_features)
        
        # Risk analizi
        risk_assessment = self._analyze_risks(story_features)
        
        # Story point tahmini
        story_points = self._predict_story_points(story_features)
        
        # Agent aksiyonu
        action = self._get_agent_action(story_features)
        
        return {
            "story_embedding": story_embedding.tolist(),
            "complexity_analysis": complexity,
            "risk_assessment": risk_assessment,
            "story_points": story_points,
            "agent_recommendation": action
        }

    async def prioritize_backlog(self, items: List[Dict[str, Any]], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Backlog öğelerini derin öğrenme ile önceliklendirir."""
        # Öğe gömme
        item_embeddings = [self._get_story_embedding(item["description"]) for item in items]
        
        # Önceliklendirme
        priorities = self._calculate_priorities(item_embeddings, context)
        
        # Agent aksiyonu
        action = self._get_agent_action(np.mean(item_embeddings, axis=0))
        
        return {
            "prioritized_items": priorities,
            "embeddings": [emb.tolist() for emb in item_embeddings],
            "agent_recommendation": action
        }

    async def analyze_sprint_performance(self, sprint_data: Dict[str, Any]) -> Dict[str, Any]:
        """Sprint performansını derin öğrenme ile analiz eder."""
        # Performans metrikleri
        metrics = self._extract_performance_metrics(sprint_data)
        
        # Velocity tahmini
        velocity_prediction = self._predict_velocity(metrics)
        
        # Risk analizi
        risk_assessment = self._analyze_sprint_risks(metrics)
        
        # Agent aksiyonu
        action = self._get_agent_action(metrics)
        
        return {
            "performance_metrics": metrics,
            "velocity_prediction": velocity_prediction,
            "risk_assessment": risk_assessment,
            "agent_recommendation": action
        }

    def _get_story_embedding(self, text: str) -> np.ndarray:
        """Metin gömme oluşturur."""
        # BERT gömme
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.bert_model(**inputs)
        bert_embedding = outputs.last_hidden_state.mean(dim=1).numpy()
        
        # Word2Vec gömme
        tokens = word_tokenize(text.lower())
        word2vec_embedding = np.mean([self.word2vec.wv[word] for word in tokens if word in self.word2vec.wv], axis=0)
        
        # Gömme birleştirme
        return np.concatenate([bert_embedding, word2vec_embedding])

    def _analyze_complexity(self, features: torch.Tensor) -> Dict[str, Any]:
        """Karmaşıklık analizi yapar."""
        complexity_scores = self.story_analyzer(features)
        return {
            "technical_complexity": float(complexity_scores[0]),
            "business_complexity": float(complexity_scores[1]),
            "integration_complexity": float(complexity_scores[2])
        }

    def _analyze_risks(self, features: torch.Tensor) -> Dict[str, Any]:
        """Risk analizi yapar."""
        risk_scores = self.risk_analyzer(features)
        return {
            "technical_risk": float(risk_scores[0]),
            "business_risk": float(risk_scores[1]),
            "schedule_risk": float(risk_scores[2])
        }

    def _predict_story_points(self, features: torch.Tensor) -> int:
        """Story point tahmini yapar."""
        prediction = self.velocity_predictor(features)
        return round(float(prediction))

    def _get_agent_action(self, state: np.ndarray) -> Dict[str, Any]:
        """RL agent'ın aksiyonunu alır."""
        action, _ = self.agent.predict(state)
        return {
            "action_type": int(action),
            "confidence": float(self.agent.policy.get_distribution(torch.FloatTensor(state)).entropy())
        }

    def train_models(self, training_data: Dict[str, Any]):
        """Modelleri eğitir."""
        # Story analyzer eğitimi
        self._train_story_analyzer(training_data["stories"])
        
        # Velocity predictor eğitimi
        self._train_velocity_predictor(training_data["velocities"])
        
        # Risk analyzer eğitimi
        self._train_risk_analyzer(training_data["risks"])
        
        # RL agent eğitimi
        self._train_agent(training_data["actions"])

    def _train_story_analyzer(self, stories: List[Dict[str, Any]]):
        """Story analyzer modelini eğitir."""
        for story in stories:
            features = torch.FloatTensor(self._get_story_embedding(story["text"]))
            target = torch.FloatTensor(story["complexity"])
            
            self.optimizer.zero_grad()
            output = self.story_analyzer(features)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

    def _train_velocity_predictor(self, velocities: List[Dict[str, Any]]):
        """Velocity predictor modelini eğitir."""
        for velocity in velocities:
            features = torch.FloatTensor(velocity["features"])
            target = torch.FloatTensor([velocity["points"]])
            
            self.optimizer.zero_grad()
            output = self.velocity_predictor(features)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

    def _train_risk_analyzer(self, risks: List[Dict[str, Any]]):
        """Risk analyzer modelini eğitir."""
        for risk in risks:
            features = torch.FloatTensor(risk["features"])
            target = torch.FloatTensor(risk["scores"])
            
            self.optimizer.zero_grad()
            output = self.risk_analyzer(features)
            loss = self.criterion(output, target)
            loss.backward()
            self.optimizer.step()

    def _train_agent(self, actions: List[Dict[str, Any]]):
        """RL agent'ı eğitir."""
        self.agent.learn(total_timesteps=1000) 