"""empty message

Revision ID: b964c0ee7c2d
Revises: e678d1081ac2
Create Date: 2020-02-19 21:27:50.931941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b964c0ee7c2d'
down_revision = 'e678d1081ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('field', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('field', 'description')
    # ### end Alembic commands ###
