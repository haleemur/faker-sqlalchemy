from _typeshed import Incomplete
from faker import Faker
from faker.providers import BaseProvider
from sqlalchemy import Column
from sqlalchemy.sql.type_api import TypeEngine
from typing import Callable, Type, TypeVar, Union

ModelType = TypeVar('ModelType')
ColumnType = TypeVar('ColumnType', bound=TypeEngine)
PrimitiveJsonTypes = Union[str, int, bool, None]
GeneratorFunction = Callable[[Faker, Column], Column]
GeneratorSpec = Union[str, GeneratorFunction]


class SqlAlchemyProvider(BaseProvider):
    MAPPINGS: Incomplete
    generator: BaseProvider
    @classmethod
    def register_type_mapping(cls, type: TypeEngine, spec: GeneratorSpec): ...
    @classmethod
    def reset_type_mappings(cls) -> None: ...
    def sqlalchemy_model(self, model: Type[ModelType], generate_primary_keys: bool = ..., generate_related: bool = ..., **overrides) -> ModelType: ...
    def sqlalchemy_column_value(self, column: Column) -> ColumnType: ...
