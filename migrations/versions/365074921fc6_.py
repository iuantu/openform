"""empty message

Revision ID: 365074921fc6
Revises: 3493f6fb2960
Create Date: 2020-02-25 23:59:29.653449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '365074921fc6'
down_revision = '3493f6fb2960'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('form_id_index', table_name='choice')
    op.add_column('constraint', sa.Column('enabled', sa.Boolean(), server_default=sa.text('true'), nullable=True))

    op.add_column('max_constraint', sa.Column('max', sa.Integer(), nullable=True))
    op.drop_column('max_constraint', 'min')


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('constraint', 'enabled')
    op.create_index('form_id_index', 'choice', ['form_id'], unique=False)

    op.add_column('max_constraint', sa.Column('min', sa.Integer(), nullable=True))
    op.drop_column('max_constraint', 'max')
    # ### end Alembic commands ###
