"""Add many-to-many relationship table 

Revision ID: 472b81495ca7
Revises: 6d2c5570c895
Create Date: 2024-02-14 23:23:53.386809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '472b81495ca7'
down_revision = '6d2c5570c895'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_users',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'customer_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant_users')
    # ### end Alembic commands ###