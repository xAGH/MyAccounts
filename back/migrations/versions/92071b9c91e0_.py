"""empty message

Revision ID: 92071b9c91e0
Revises: 5d11294eec2d
Create Date: 2022-04-21 18:29:10.591482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92071b9c91e0'
down_revision = '5d11294eec2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###