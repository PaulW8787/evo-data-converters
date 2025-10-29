from evo.objects.utils.data import ObjectDataClient
from evo_schemas.components import (
    ContinuousAttribute_V1_1_0 as ContinuousAttribute,
    NanContinuous_V1_0_1 as NanContinuous,
    OneOfAttribute_V1_2_0_Item as OneOfAttribute_Item,
)
from evo_schemas.elements import (
    FloatArray1_V1_0_1 as FloatArray1,
)

import pandas as pd
import pyarrow as pa
import typing


class PyArrowTableFactory:
    @staticmethod
    def create_continuous_table(series: pd.Series) -> pa.Table:
        schema = pa.schema([("data", pa.float64())])
        return pa.Table.from_pandas(series.rename("data").to_frame(), schema=schema)


class AttributeFactory:
    @staticmethod
    def create(name: str, series: pd.Series, client: ObjectDataClient) -> OneOfAttribute_Item | None:
        nan_values_list: list[typing.Any] = list(series.attrs["nan_values"]) if "nan_values" in series.attrs else []

        if pd.api.types.is_float_dtype(series):
            table = PyArrowTableFactory.create_continuous_table(series)
            table_info = client.save_table(table)
            float_array = FloatArray1.from_dict(table_info)
            return ContinuousAttribute(
                key=name,
                name=name,
                nan_description=NanContinuous(values=nan_values_list),
                values=float_array,
            )

        else:
            return None
