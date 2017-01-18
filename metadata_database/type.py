import sqlalchemy.types
import uuid


class UUID(sqlalchemy.types.TypeDecorator):
    impl = sqlalchemy.types.BINARY(16)

    python_type = uuid.UUID

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(self.impl)

    def process_bind_param(self, value, dialect):
        if value is None:
            return value

        if not isinstance(value, uuid.UUID):
            if value and not isinstance(value, uuid.UUID):
                try:
                    value = uuid.UUID(value)
                except (TypeError, ValueError):
                    value = uuid.UUID(bytes=value)

        return value.bytes

    def process_literal_param(self, value, dialect):
        pass

    def process_result_value(self, value, dialect):
        if value is None:
            return value

        return uuid.UUID(bytes=value)
