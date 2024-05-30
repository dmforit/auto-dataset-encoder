# -*- coding: utf-8 -*-
################################################################################
#     dataset_encoder for AutoML systems 
#     Python v3.8+
#     Created by dmforit
#     Licensed under Apache License v2
################################################################################
# Version
from .__version__ import __version__
from .categorical_encoder import CategoricalEncoder
from .circular_encoder import CircularEncoder
from .datetime_encoder import DateTimeEncoder
from .numerical_encoder import NumericalEncoder
from .encoder import Encoder
################################################################################
if __name__ == "__main__":
    module_type = 'Running'
else:
    module_type = 'Imported'
version_number = __version__
print("""%s featurewiz %s. Use the following syntax:
    >>> enc = Encoder(categorical_args=None, numerical_args=None, 
      datetime_args=None, categorical_enabled=True, numerical_enabled=True, 
      datetime_enabled=True, target_enabled=False, target_encoder='label', keep_df=False)
    >>> X_train_processed, y_train_processed = enc.fit_transform(X_train, y_train)
    >>> X_test_processed = enc.transform(X_test)
    """ %(module_type, version_number))
################################################################################