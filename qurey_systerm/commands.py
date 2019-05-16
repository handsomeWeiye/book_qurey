from qurey_systerm import app,db
from qurey_systerm.models import Data
import click


@app.cli.command()
@click.option('--count',default=20 ,help='Quantity of fake dada,dafult number is 20')
def forge(count):
    db.drop_all()
    db.create_all()
    from faker import Faker
    fake = Faker('zh_CN')
    click.echo('working...')

    for i in range(count):
        data = Data(
            author=fake.name(),
            book=fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(data)
    db.session.commit()

    click.echo('you have mada %s faker datas.'%count)




