from .dataframe import DataframeConvertFeatureGenerator
from .binned import BinnedFeatureGenerator
from .category import CategoryFeatureGenerator
from .datetime import DatetimeFeatureGenerator
from .drop_duplicates import DropDuplicatesFeatureGenerator
from .fillna import FillNaFeatureGenerator
from .statics import StatisticsFeatureGenerator
from .type import TypeInferFeatureGenerator
from .encoder import LabelEncoderFeatureGenerator, OneHotEncoderFeatureGenerator
from .nlp import TextFeatureGenerator
from .geograph import GeoFeatureGenerator, CoordinatesInferFeatureGenerator

pre_feature_generator_list = [
    FillNaFeatureGenerator,
    TypeInferFeatureGenerator,
    CoordinatesInferFeatureGenerator,
]

transformation_generator_list = [
    DatetimeFeatureGenerator,
    GeoFeatureGenerator,
    TextFeatureGenerator,
]

index_generator_list = [
    BinnedFeatureGenerator,
    CategoryFeatureGenerator,
]

encode_generator_list = [
    LabelEncoderFeatureGenerator,
    OneHotEncoderFeatureGenerator
]

post_feature_generator_list = []