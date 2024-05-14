"""Initial migration

Revision ID: d70188913967
Revises: 
Create Date: 2024-05-15 03:03:35.199882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70188913967'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.String(), nullable=True),
    sa.Column('receiver_id', sa.String(), nullable=True),
    sa.Column('conversation_id', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('created_at', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_id'), 'chat', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_chat_id'), table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###
