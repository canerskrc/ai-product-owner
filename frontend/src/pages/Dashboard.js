import React from 'react';
import {
  Box,
  Grid,
  Card,
  CardContent,
  Typography,
  LinearProgress,
  useTheme,
} from '@mui/material';
import {
  Timeline,
  TimelineItem,
  TimelineSeparator,
  TimelineConnector,
  TimelineContent,
  TimelineDot,
} from '@mui/lab';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

const data = [
  { name: 'Sprint 1', completed: 85, planned: 100 },
  { name: 'Sprint 2', completed: 90, planned: 100 },
  { name: 'Sprint 3', completed: 75, planned: 100 },
  { name: 'Sprint 4', completed: 95, planned: 100 },
];

const recentActivities = [
  {
    title: 'New User Story Created',
    description: 'User authentication system implementation',
    time: '2 hours ago',
    type: 'story',
  },
  {
    title: 'Sprint Completed',
    description: 'Sprint 4 completed with 95% success rate',
    time: '1 day ago',
    type: 'sprint',
  },
  {
    title: 'Task Assigned',
    description: 'Password reset functionality assigned to John',
    time: '2 days ago',
    type: 'task',
  },
];

const StatCard = ({ title, value, subtitle, color }) => {
  const theme = useTheme();
  return (
    <Card sx={{ height: '100%' }}>
      <CardContent>
        <Typography color="textSecondary" gutterBottom>
          {title}
        </Typography>
        <Typography variant="h4" component="div" sx={{ color: theme.palette[color].main }}>
          {value}
        </Typography>
        <Typography variant="body2" color="textSecondary">
          {subtitle}
        </Typography>
      </CardContent>
    </Card>
  );
};

const Dashboard = () => {
  const theme = useTheme();

  return (
    <Box>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        {/* İstatistik Kartları */}
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Active Projects"
            value="12"
            subtitle="3 projects completed this month"
            color="primary"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Team Velocity"
            value="85%"
            subtitle="+5% from last sprint"
            color="success"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Open Tasks"
            value="24"
            subtitle="8 tasks due this week"
            color="warning"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <StatCard
            title="Team Members"
            value="8"
            subtitle="2 new members this month"
            color="secondary"
          />
        </Grid>

        {/* Sprint Progress Chart */}
        <Grid item xs={12} md={8}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Sprint Progress
              </Typography>
              <Box sx={{ height: 300 }}>
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="completed" fill={theme.palette.primary.main} />
                    <Bar dataKey="planned" fill={theme.palette.primary.light} />
                  </BarChart>
                </ResponsiveContainer>
              </Box>
            </CardContent>
          </Card>
        </Grid>

        {/* Recent Activities */}
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Recent Activities
              </Typography>
              <Timeline>
                {recentActivities.map((activity, index) => (
                  <TimelineItem key={index}>
                    <TimelineSeparator>
                      <TimelineDot color={
                        activity.type === 'story' ? 'primary' :
                        activity.type === 'sprint' ? 'success' :
                        'warning'
                      } />
                      {index < recentActivities.length - 1 && <TimelineConnector />}
                    </TimelineSeparator>
                    <TimelineContent>
                      <Typography variant="subtitle2">{activity.title}</Typography>
                      <Typography variant="body2" color="textSecondary">
                        {activity.description}
                      </Typography>
                      <Typography variant="caption" color="textSecondary">
                        {activity.time}
                      </Typography>
                    </TimelineContent>
                  </TimelineItem>
                ))}
              </Timeline>
            </CardContent>
          </Card>
        </Grid>

        {/* Team Performance */}
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Team Performance
              </Typography>
              <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                  <Typography variant="subtitle2" gutterBottom>
                    Sprint Velocity
                  </Typography>
                  <LinearProgress
                    variant="determinate"
                    value={85}
                    sx={{
                      height: 10,
                      borderRadius: 5,
                      backgroundColor: theme.palette.primary.light,
                      '& .MuiLinearProgress-bar': {
                        backgroundColor: theme.palette.primary.main,
                      },
                    }}
                  />
                </Grid>
                <Grid item xs={12} md={6}>
                  <Typography variant="subtitle2" gutterBottom>
                    Code Quality
                  </Typography>
                  <LinearProgress
                    variant="determinate"
                    value={92}
                    sx={{
                      height: 10,
                      borderRadius: 5,
                      backgroundColor: theme.palette.success.light,
                      '& .MuiLinearProgress-bar': {
                        backgroundColor: theme.palette.success.main,
                      },
                    }}
                  />
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard; 