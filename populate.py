import random

from sqlmodel import Session

from models.gem_models import Gem, GemProperties, GemType, GemColor
from utils.db_utils import get_engine_from_settings

engine = get_engine_from_settings()
color_multiplier = {
    'D': 1.8,
    'E': 1.6,
    'G': 1.4,
    'F': 1.2,
    'H': 1,
    'I': 0.8,
}


def calculate_gem_price(gem, gem_pr):
    price = 1000
    if gem.gem_type == 'RUBY':
        price = 400
    elif gem.gem_type == 'EMERALD':
        price = 650

    if gem_pr.clarity == 1:
        price *= 0.75
    elif gem_pr.clarity == 3:
        price *= 1.25
    elif gem_pr.clarity == 4:
        price *= 1.5

    price *= (gem_pr.size ** 3)

    if gem.gem_type == 'DIAMOND':
        multiplier = color_multiplier[gem_pr.color]
        price *= multiplier

    return round(price, 2)


def create_gem_props():
    size = random.randint(3, 70) / 10
    color = random.choice(GemColor.list())
    clarity = random.randint(1, 4)
    gem_p = GemProperties(size=size, clarity=clarity,
                          color=color)
    return gem_p


def create_gem(gem_p):
    gem_type = random.choice(GemType.list())
    gem = Gem(price=1000, gem_properties_id=gem_p.id, gem_type=gem_type)
    price = calculate_gem_price(gem, gem_p)
    gem.price = price
    return gem


def create_gems_db():
    # gem_p = create_gem_props()
    gem_ps = [create_gem_props() for x in range(100)]
    with Session(engine) as session:
        session.add_all(gem_ps)
        session.commit()
        gems = [create_gem(gem_ps[x]) for x in range(100)]
        session.add_all(gems)
        # g = create_gem(gem_p.id)
        # session.add(g)
        session.commit()


if __name__ == '__main__':
    create_gems_db()
