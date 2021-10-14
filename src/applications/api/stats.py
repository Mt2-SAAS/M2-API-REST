from django.db import connections


class Stats:
    """
    Helper class for retrive stats from database
    """

    def __init__(self):
        pass

    @staticmethod
    def create_cursor(database: str):
        """
        Cursor for database query direct
        """
        cursor = connections[database].cursor()
        return cursor

    def get_last(self, minutes: str, interval="MINUTE"):
        """
        Get last connections players
        """
        cursor = self.create_cursor("player")
        query = f"""
            SELECT COUNT(*) as count
            FROM player 
            WHERE DATE_SUB(NOW(), INTERVAL {minutes} {interval}) < last_play
        """

        cursor.execute(query)
        query_response = cursor.fetchall()[0][0]
        return query_response

    def get_count(self, database):
        cursor = self.create_cursor(database)
        query = f"SELECT COUNT(*) from {database}"

        cursor.execute(query)
        response = cursor.fetchall()[0][0]
        return response

    def get_format_stats(self):
        online = self.get_last("5")
        lastonline = self.get_last("24", interval="HOUR")
        accounts = self.get_count("account")
        players = self.get_count("player")
        return {
            "online": online,
            "lastonline": lastonline,
            "accounts": accounts,
            "players": players,
        }
