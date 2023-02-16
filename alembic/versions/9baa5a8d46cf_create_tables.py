"""create tables

Revision ID: 9baa5a8d46cf
Revises: 
Create Date: 2023-02-15 21:22:26.437728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9baa5a8d46cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_created_at'), 'product', ['created_at'], unique=False)
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_table('role',
    sa.Column('role_name', sa.String(length=200), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_created_at'), 'role', ['created_at'], unique=False)
    op.create_index(op.f('ix_role_id'), 'role', ['id'], unique=False)
    op.create_table('user',
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_created_at'), 'user', ['created_at'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_role_id'), 'user', ['role_id'], unique=False)
    op.create_table('sale',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sale_created_at'), 'sale', ['created_at'], unique=False)
    op.create_index(op.f('ix_sale_id'), 'sale', ['id'], unique=False)
    op.create_index(op.f('ix_sale_user_id'), 'sale', ['user_id'], unique=False)
    op.create_table('shopping_card',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shopping_card_created_at'), 'shopping_card', ['created_at'], unique=False)
    op.create_index(op.f('ix_shopping_card_id'), 'shopping_card', ['id'], unique=False)
    op.create_index(op.f('ix_shopping_card_user_id'), 'shopping_card', ['user_id'], unique=False)
    op.create_table('element_cart',
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['shopping_card.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_element_cart_cart_id'), 'element_cart', ['cart_id'], unique=False)
    op.create_index(op.f('ix_element_cart_created_at'), 'element_cart', ['created_at'], unique=False)
    op.create_index(op.f('ix_element_cart_id'), 'element_cart', ['id'], unique=False)
    op.create_index(op.f('ix_element_cart_product_id'), 'element_cart', ['product_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_element_cart_product_id'), table_name='element_cart')
    op.drop_index(op.f('ix_element_cart_id'), table_name='element_cart')
    op.drop_index(op.f('ix_element_cart_created_at'), table_name='element_cart')
    op.drop_index(op.f('ix_element_cart_cart_id'), table_name='element_cart')
    op.drop_table('element_cart')
    op.drop_index(op.f('ix_shopping_card_user_id'), table_name='shopping_card')
    op.drop_index(op.f('ix_shopping_card_id'), table_name='shopping_card')
    op.drop_index(op.f('ix_shopping_card_created_at'), table_name='shopping_card')
    op.drop_table('shopping_card')
    op.drop_index(op.f('ix_sale_user_id'), table_name='sale')
    op.drop_index(op.f('ix_sale_id'), table_name='sale')
    op.drop_index(op.f('ix_sale_created_at'), table_name='sale')
    op.drop_table('sale')
    op.drop_index(op.f('ix_user_role_id'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_created_at'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_role_id'), table_name='role')
    op.drop_index(op.f('ix_role_created_at'), table_name='role')
    op.drop_table('role')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_index(op.f('ix_product_created_at'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###