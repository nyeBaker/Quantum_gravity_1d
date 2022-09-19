import numpy as np
import sympy

from einsteinpy.symbolic.helpers import _change_name
from einsteinpy.symbolic.tensor import BaseRelativityTensor, _change_config


class veilbeins(BaseRelativityTensor):
    """
    Class for defining Veilbeins.
    """

    def __init__(
        self, arr, syms, config="ul", parent_metric=None, name="Veilbein"
    ):
        """
        Constructor and Initializer

        Parameters
        ----------
        arr : ~sympy.tensor.array.dense_ndim_array.ImmutableDenseNDimArray or list
            Sympy Array or multi-dimensional list containing Sympy Expressions
        syms : tuple or list
            Tuple of crucial symbols denoting time-axis, 1st, 2nd, and 3rd axis (t,x1,x2,x3)
        config : str
            Configuration of contravariant and covariant indices in tensor. 'u' for upper and 'l' for lower indices. Defaults to 'ull'.
        parent_metric : ~einsteinpy.symbolic.metric.MetricTensor
            Metric Tensor from which veilbein is calculated. Defaults to None.
        name : str
            Name of the veilbein Tensor. Defaults to "Veilbein".

        Raises
        ------
        TypeError
            Raised when arr is not a list or sympy Array
        TypeError
            syms is not a list or tuple
        ValueError
            config has more or less than 3 indices

        """
        super(veilbeins, self).__init__(
            arr=arr, syms=syms, config=config, parent_metric=parent_metric, name=name
        )
        self._order = 3
        if not len(self.config) == self._order:
            raise ValueError("config should be of length {}".format(self._order))
    @classmethod
    def from_metric(self, metric):
        """
        Calculate the veilbeins from the metric tensor. Veilbeins are the difference between a 

        Parameters
        ----------
        metric : ~einsteinpy.symbolic.metric.MetricTensor
            Space-time Metric from which veilbeins are to be calculated
        
        """

        dims = metric.dims
        veilbein = np.zeros((dims,dims),dtype=int).tolist()
        mat = metric.lower_config().tensor()

        for t in range(dims):
            for tt in range(dims):
                tmp = 0
                tmp += sympy.sqrt(mat[t,tt])

                veilbein[t][tt] = tmp
        
        return veilbein

