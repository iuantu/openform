"""empty message

Revision ID: 9ba7c1863ed2
Revises: b5c3bfe4f980
Create Date: 2019-12-28 17:11:05.963230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ba7c1863ed2'
down_revision = 'b5c3bfe4f980'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('constraint',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=True),
    sa.Column('discriminator', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('max_constraint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['constraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('min_constraint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['constraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('range_constraint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.Column('max', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['constraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('required_constraint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['constraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('select_field', sa.Column('option_sequence', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('select_field', 'option_sequence')
    op.drop_table('required_constraint')
    op.drop_table('range_constraint')
    op.drop_table('min_constraint')
    op.drop_table('max_constraint')
    op.drop_table('constraint')
    # ### end Alembic commands ###
