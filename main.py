import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", encoding="utf-8") as f:
        players = json.load(f)

        for player in players:
            race, _ = Race.objects.get_or_create(
                name=player["race"]["name"],
                defaults={"description": player["race"].get("description", "")}
            )

            for skill in player["race"].get("skills", []):
                Skill.objects.get_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race
                    }
                )

            guild_data = player.get("guild")
            guild = None
            if guild_data:
                guild, _ = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={"description": guild_data.get("description")}
                )

            Player.objects.get_or_create(
                nickname=player["nickname"],
                defaults={
                    "email": player["email"],
                    "bio": player["bio"],
                    "race": race,
                    "guild": guild
                }
            )


if __name__ == "__main__":
    main()
