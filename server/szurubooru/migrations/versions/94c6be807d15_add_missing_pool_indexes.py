"""
Add missing pool indexes

Revision ID: 94c6be807d15
Created at: 2026-09-29 12:00:00.000000
"""

from alembic import op

revision = "94c6be807d15"
down_revision = "5b5c940b4e78"
branch_labels = None
depends_on = None

# The models declare these indexes, but the migration that created the pool
# tables did not. Some instances added them by hand, hence if_not_exists.
# pool_post.pool_id needs no index of its own: it leads the primary key.
INDEXES = [
    ("ix_pool_name_pool_id", "pool_name", "pool_id"),
    ("ix_pool_category_id", "pool", "category_id"),
]


def upgrade():
    for index_name, table_name, column_name in INDEXES:
        op.create_index(
            op.f(index_name),
            table_name,
            [column_name],
            unique=False,
            if_not_exists=True,
        )


def downgrade():
    for index_name, table_name, _column_name in reversed(INDEXES):
        op.drop_index(op.f(index_name), table_name=table_name, if_exists=True)
