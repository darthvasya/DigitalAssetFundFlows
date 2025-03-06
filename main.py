# main.py
from database import init_db, get_db
from database.models import Country, Institution, Asset, Flow

init_db()

def create_data():
    db = next(get_db())
    try:
        country = Country(name="Australia")
        db.add(country)
        db.commit()

        institution = Institution(name="PROSHARES BITCOIN ETF-USD", country=country)
        db.add(institution)
        db.commit()

        asset = Asset(name="BITCOIN")
        db.add(asset)
        db.commit()

        asset = Asset(name="ETH")
        db.add(asset)
        db.commit()

        asset = Asset(name="ETH1")
        db.add(asset)
        db.commit()

        flow = Flow(amount=75, date="2023-10-01", asset=asset, institution=institution)
        db.add(flow)
        db.commit()

        print("Данные добавлены!")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    create_data()