"""empty message

Revision ID: d0750604e4d3
Revises: 
Create Date: 2020-10-02 13:01:43.615765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0750604e4d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('rent', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_property_address'), 'property', ['address'], unique=True)
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=150), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('isComplete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    op.drop_index(op.f('ix_property_address'), table_name='property')
    op.drop_table('property')
    # ### end Alembic commands ###