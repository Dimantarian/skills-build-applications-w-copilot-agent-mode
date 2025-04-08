from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from bson import ObjectId

print('populate_db command loaded')

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        users = [User(**user) for user in test_users]
        User.objects.bulk_create(users)

        # Populate teams
        teams = [Team(**team) for team in test_teams]
        Team.objects.bulk_create(teams)

        # Populate activities
        for activity, user in zip(test_activities, users):
            activity['user'] = user
        activities = [Activity(**activity) for activity in test_activities]
        Activity.objects.bulk_create(activities)

        # Populate leaderboard
        for entry, user in zip(test_leaderboard, users):
            entry['user'] = user
        leaderboard_entries = [Leaderboard(**entry) for entry in test_leaderboard]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Populate workouts
        workouts = [Workout(**workout) for workout in test_workouts]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))