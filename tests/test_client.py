import unittest

from config import (
    access_token, access_token_secret, bearer_token, consumer_key,
    consumer_secret, tape, user_id
)
import tweepy


class TweepyTestCase(unittest.TestCase):

    def setUp(self):
        self.client = tweepy.Client(
            bearer_token, consumer_key, consumer_secret,
            access_token or user_id, access_token_secret
        )

    @tape.use_cassette("test_bookmarks.yaml", serializer="yaml")
    def test_bookmarks(self):
        tweet_id = 1507070437557096461
        # @TwitterDev Tweet announcing API v2 Bookmarks endpoints
        self.client.bookmark(tweet_id)
        self.client.get_bookmarks()
        self.client.remove_bookmark(tweet_id)

    @tape.use_cassette("test_hide_and_unhide_reply.yaml", serializer="yaml")
    def test_hide_and_unhide_reply(self):
        reply_id = 1344794616005066752  # Test Tweet for reply hide/unhide
        self.client.hide_reply(reply_id)
        self.client.unhide_reply(reply_id)

    @tape.use_cassette("test_like_and_unlike.yaml", serializer="yaml")
    def test_like_and_unlike(self):
        tweet_id = 1293593516040269825  # @TwitterDev Tweet announcing API v2
        self.client.like(tweet_id)
        self.client.unlike(tweet_id)

    @tape.use_cassette("test_get_liking_users.yaml", serializer="yaml")
    def test_get_liking_users(self):
        tweet_id = 1293593516040269825  # @TwitterDev Tweet announcing API v2
        self.client.get_liking_users(tweet_id)

    @tape.use_cassette("test_get_liked_tweets.yaml", serializer="yaml")
    def test_get_liked_tweets(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_liked_tweets(user_id)

    @tape.use_cassette("test_create_and_delete_tweet.yaml", serializer="yaml")
    def test_create_and_delete_tweet(self):
        response = self.client.create_tweet(text="Test Tweet")
        tweet_id = response.data["id"]
        self.client.delete_tweet(tweet_id)

    @tape.use_cassette("test_get_quote_tweets.yaml", serializer="yaml")
    def test_get_quote_tweets(self):
        tweet_id = 1293593516040269825  # @TwitterDev Tweet announcing API v2
        self.client.get_quote_tweets(tweet_id)

    @tape.use_cassette("test_retweet_and_unretweet.yaml", serializer="yaml")
    def test_retweet_and_unretweet(self):
        tweet_id = 1415348607813832708
        # @TwitterDev Tweet announcing API v2 Retweet endpoints
        self.client.retweet(tweet_id)
        self.client.unretweet(tweet_id)

    @tape.use_cassette("test_get_retweeters.yaml", serializer="yaml")
    def test_get_retweeters(self):
        tweet_id = 1415348607813832708
        # @TwitterDev Tweet announcing API v2 Retweet endpoints
        self.client.get_retweeters(tweet_id)

    @tape.use_cassette("test_search_all_tweets.yaml", serializer="yaml")
    def test_search_all_tweets(self):
        self.client.search_all_tweets("Tweepy")

    @tape.use_cassette("test_search_recent_tweets.yaml", serializer="yaml")
    def test_search_recent_tweets(self):
        self.client.search_recent_tweets("Tweepy")

    @tape.use_cassette("test_get_users_mentions.yaml", serializer="yaml")
    def test_get_users_mentions(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_users_mentions(user_id)

    @tape.use_cassette("test_get_users_tweets.yaml", serializer="yaml")
    def test_get_users_tweets(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_users_tweets(user_id)

    @tape.use_cassette("test_get_all_tweets_count.yaml", serializer="yaml")
    def test_get_all_tweets_count(self):
        self.client.get_all_tweets_count("Tweepy")

    @tape.use_cassette("test_get_recent_tweets_count.yaml", serializer="yaml")
    def test_get_recent_tweets_count(self):
        self.client.get_recent_tweets_count("Tweepy")

    @tape.use_cassette("test_get_tweet.yaml", serializer="yaml")
    def test_get_tweet(self):
        tweet_id = 1293593516040269825  # @TwitterDev Tweet announcing API v2
        self.client.get_tweet(tweet_id)

    @tape.use_cassette("test_get_tweets.yaml", serializer="yaml")
    def test_get_tweets(self):
        tweet_ids = [1293593516040269825, 1293595870563381249]
        # @TwitterDev and @TwitterAPI Tweets announcing API v2
        self.client.get_tweets(tweet_ids)

    @tape.use_cassette("test_block_and_get_blocked_and unblock.yaml",
                       serializer="yaml")
    def test_block_and_unblock(self):
        user_id = 17874544  # User ID for @TwitterSupport
        self.client.block(user_id)
        self.client.get_blocked()
        self.client.unblock(user_id)

    @tape.use_cassette("test_follow_and_unfollow_user.yaml", serializer="yaml")
    def test_follow_and_unfollow_user(self):
        user_id = 17874544  # User ID for @TwitterSupport
        self.client.follow_user(user_id)
        self.client.unfollow_user(user_id)

    @tape.use_cassette("test_get_users_followers.yaml", serializer="yaml")
    def test_get_users_followers(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_users_followers(user_id)

    @tape.use_cassette("test_get_users_following.yaml", serializer="yaml")
    def test_get_users_following(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_users_following(user_id)

    @tape.use_cassette("test_mute_get_muted_and_unmute.yaml",
                       serializer="yaml")
    def test_mute_get_muted_and_unmute(self):
        user_id = 17874544  # User ID for @TwitterSupport
        self.client.mute(user_id)
        self.client.get_muted()
        self.client.unmute(user_id)

    @tape.use_cassette("test_get_user.yaml", serializer="yaml")
    def test_get_user(self):
        self.client.get_user(username="Twitter")

    @tape.use_cassette("test_get_users.yaml", serializer="yaml")
    def test_get_users(self):
        self.client.get_users(usernames=["Twitter", "TwitterDev"])

    @tape.use_cassette("test_get_me.yaml", serializer="yaml")
    def test_get_me(self):
        self.client.get_me()

    @tape.use_cassette("test_search_spaces.yaml", serializer="yaml")
    def test_search_spaces(self):
        self.client.search_spaces("Twitter")

    @tape.use_cassette("test_get_spaces.yaml", serializer="yaml")
    def test_get_spaces(self):
        space_ids = ["1YpKkzBgBlVxj", "1OwGWzarWnNKQ"]
        # Space ID for @TwitterSpaces Twitter Spaces community gathering + Q&A
        # https://twitter.com/TwitterSpaces/status/1436382283347283969
        # Space ID for @NASA #NASAWebb Space Telescope 101 and Q&A
        # https://twitter.com/NASA/status/1442961745098653701
        user_ids = [1065249714214457345, 2328002822]
        # User IDs for @TwitterSpaces and @TwitterWomen
        self.client.get_spaces(ids=space_ids)
        self.client.get_spaces(user_ids=user_ids)

    @tape.use_cassette("test_get_space.yaml", serializer="yaml")
    def test_get_space(self):
        space_id = "1YpKkzBgBlVxj"
        # Space ID for @TwitterSpaces Twitter Spaces community gathering + Q&A
        # https://twitter.com/TwitterSpaces/status/1436382283347283969
        self.client.get_space(space_id)

    # TODO: Test Client.get_space_buyers

    # TODO: Test Client.get_space_tweets

    @tape.use_cassette("test_get_list_tweets.yaml", serializer="yaml")
    def test_get_list_tweets(self):
        list_id = 84839422  # List ID for Official Twitter Accounts (@Twitter)
        self.client.get_list_tweets(list_id)

    @tape.use_cassette("test_follow_and_unfollow_list.yaml", serializer="yaml")
    def test_follow_and_unfollow_list(self):
        list_id = 84839422  # List ID for Official Twitter Accounts (@Twitter)
        self.client.follow_list(list_id)
        self.client.unfollow_list(list_id)

    @tape.use_cassette("test_get_list_followers.yaml", serializer="yaml")
    def test_get_list_followers(self):
        list_id = 84839422  # List ID for Official Twitter Accounts (@Twitter)
        self.client.get_list_followers(list_id)

    @tape.use_cassette("test_get_followed_lists.yaml", serializer="yaml")
    def test_get_followed_lists(self):
        user_id = 372575989  # User ID for @TwitterNews
        self.client.get_followed_lists(user_id)

    @tape.use_cassette("test_get_list.yaml", serializer="yaml")
    def test_get_list(self):
        list_id = 84839422  # List ID for Official Twitter Accounts (@Twitter)
        self.client.get_list(list_id)

    @tape.use_cassette("test_get_owned_lists.yaml", serializer="yaml")
    def test_get_owned_lists(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_owned_lists(user_id)

    @tape.use_cassette("test_get_list_members.yaml", serializer="yaml")
    def test_get_list_members(self):
        list_id = 84839422  # List ID for Official Twitter Accounts (@Twitter)
        self.client.get_list_members(list_id)

    @tape.use_cassette("test_get_list_memberships.yaml", serializer="yaml")
    def test_get_list_memberships(self):
        user_id = 783214  # User ID for @Twitter
        self.client.get_list_memberships(user_id)

    @tape.use_cassette("test_manage_and_get_pinned_lists.yaml",
                       serializer="yaml")
    def test_manage_and_get_pinned_lists(self):
        response = self.client.create_list("Test List", private=True)
        list_id = response.data["id"]
        user_id = 783214  # User ID for @Twitter
        self.client.add_list_member(list_id, user_id)
        self.client.pin_list(list_id)
        self.client.get_pinned_lists()
        self.client.remove_list_member(list_id, user_id)
        self.client.unpin_list(list_id)
        self.client.update_list(list_id, description="Test List Description")
        self.client.delete_list(list_id)

    @tape.use_cassette("test_create_and_get_compliance_job_and_jobs.yaml",
                       serializer="yaml")
    def test_create_and_get_compliance_job_and_jobs(self):
        response = self.client.create_compliance_job("tweets")
        job_id = response.data["id"]
        self.client.get_compliance_job(job_id)
        self.client.get_compliance_jobs("tweets")
