import numpy as np
import sympy

from einsteinpy.symbolic.helpers import _change_name
from einsteinpy.symbolic.tensor import BaseRelativityTensor, _change_config
from einsteinpy.symbolic import veilbeins, christoffel


class spinConnections(BaseRelativityTensor):
    """
    Class for defining Veilbeins.
    """

    def __init__(
        self, arr, syms, config="ull", parent_metric=None, name="spinConnection"
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
            Metric Tensor from which spin connection is calculated. Defaults to None.
        name : str
            Name of the spin Connection. Defaults to "spinConnection".

        Raises
        ------
        TypeError
            Raised when arr is not a list or sympy Array
        TypeError
            syms is not a list or tuple
        ValueError
            config has more or less than dims indices

        """
        super(spinConnections, self).__init__(
            arr=arr, syms=syms, config=config, parent_metric=parent_metric, name=name
        )
        self._order = 3
        if not len(self.config) == self._order:
            raise ValueError("config should be of length {}".format(self._order))
        #Not entirely sure what is happening here???
    @classmethod
    def from_metric(self, metric):
        """
        Calculate the spin connection from the metric tensor. 

        Parameters
        ----------
        metric : ~einsteinpy.symbolic.metric.MetricTensor
            Space-time Metric from which spin connections are to be calculated
        
        """

        # First we need to calcualte the christoffel symbol and the veilbeins

        dims = metric.dims
        chl = christoffel.from_metric(metric).tensor()
        e = veilbeins.from_metric(metric).tensor()

        tmplist = np.zeros((dims,dims,dims),dtype = int).tolist()

        for t in range(dims ** 3):
            # i,j,k each goes from 0 to (dims-1)
            k = t % dims
            j = (int(t / dims)) % (dims)
            i = (int(t / (dims ** 2))) % (dims)

            # We can take advantage of the fact that the spin connections are antismmetric

            








        
        
        return veilbein

