from sqlalchemy import text

from app.database.database import engine


class TelemetryService:

    @staticmethod
    def get_latest(limit: int = 20):

        query = text("""
            SELECT
                vehicle_id,
                latitude,
                longitude,
                speed,
                fuel_level,
                event_timestamp
            FROM vehicle_telemetry
            ORDER BY event_timestamp DESC
            LIMIT :limit
        """)

        with engine.connect() as connection:

            result = connection.execute(
                query,
                {"limit": limit}
            )

            rows = result.mappings().all()

            return rows