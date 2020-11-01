"""empty message

Revision ID: 9a81ae94dfce
Revises: c3c31f65a017
Create Date: 2020-11-01 04:03:19.546882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a81ae94dfce'
down_revision = 'c3c31f65a017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('site_url', sa.String(length=64), nullable=True),
    sa.Column('asin', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gg_created_at'), 'gg', ['created_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_gg_created_at'), table_name='gg')
    op.drop_table('gg')
    # ### end Alembic commands ###
