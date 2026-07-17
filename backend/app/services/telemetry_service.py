from sqlalchemy import text

from app.database.database import engine


class TelemetryService:

    @staticmethod
    def get_latest(limit: int = 20):

        query = text("""
            SELECT DISTINCT ON (vehicle_id)
                vehicle_id,
                driver_id,
                delivery_id,

                latitude,
                longitude,
                speed,
                fuel_level,
                remaining_distance_km,
                eta_minutes,
                status,
                event_timestamp
            FROM vehicle_telemetry
            ORDER BY vehicle_id, event_timestamp DESC
        """)

        with engine.connect() as connection:

            result = connection.execute(
                query,
                {"limit": limit}
            )

            rows = result.mappings().all()

            return rows