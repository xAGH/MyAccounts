"""empty message

Revision ID: 5d11294eec2d
Revises: 78fda368e8c3
Create Date: 2022-04-20 20:45:23.270893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d11294eec2d'
down_revision = '78fda368e8c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_login', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_login')
    # ### end Alembic commands ###
