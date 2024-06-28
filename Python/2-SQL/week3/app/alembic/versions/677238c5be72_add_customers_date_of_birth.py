"""add customers date_of_birth

Revision ID: 677238c5be72
Revises: 01eb7480be38
Create Date: 2024-06-28 14:29:35.455735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '677238c5be72'
down_revision: Union[str, None] = '01eb7480be38'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
