"""empty message

Revision ID: 85db47668d9c
Revises: 4f357c4fa151
Create Date: 2020-11-01 18:21:07.473030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85db47668d9c'
down_revision = '4f357c4fa151'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('asins', sa.Column('description', sa.String(length=200), nullable=True))
    op.add_column('asins', sa.Column('status', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('asins', 'status')
    op.drop_column('asins', 'description')
    # ### end Alembic commands ###