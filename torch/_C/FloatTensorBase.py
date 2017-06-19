# encoding: utf-8
# module torch._C
# from /Users/rook/anaconda/lib/python3.6/site-packages/torch/_C.cpython-36m-darwin.so
# by generator 1.145
# no doc

# imports
import torch._C._functions as _functions # <module 'torch._C._functions'>

from .object import object

class FloatTensorBase(object):
    # no doc
    def abs(self): # real signature unknown; restored from __doc__
        """
        abs() -> Tensor
        
        See :func:`torch.abs`
        """
        pass

    def abs_(self): # real signature unknown; restored from __doc__
        """
        abs_() -> Tensor
        
        In-place version of :meth:`~Tensor.abs`
        """
        pass

    def acos(self): # real signature unknown; restored from __doc__
        """
        acos() -> Tensor
        
        See :func:`torch.acos`
        """
        pass

    def acos_(self): # real signature unknown; restored from __doc__
        """
        acos_() -> Tensor
        
        In-place version of :meth:`~Tensor.acos`
        """
        pass

    def add(self, value): # real signature unknown; restored from __doc__
        """
        add(value)
        
        See :func:`torch.add`
        """
        pass

    def addbmm(self, beta=1, mat, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        addbmm(beta=1, mat, alpha=1, batch1, batch2) -> Tensor
        
        See :func:`torch.addbmm`
        """
        pass

    def addbmm_(self, beta=1, mat, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        addbmm_(beta=1, mat, alpha=1, batch1, batch2) -> Tensor
        
        In-place version of :meth:`~Tensor.addbmm`
        """
        pass

    def addcdiv(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcdiv(value=1, tensor1, tensor2) -> Tensor
        
        See :func:`torch.addcdiv`
        """
        pass

    def addcdiv_(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcdiv_(value=1, tensor1, tensor2) -> Tensor
        
        In-place version of :meth:`~Tensor.addcdiv`
        """
        pass

    def addcmul(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcmul(value=1, tensor1, tensor2) -> Tensor
        
        See :func:`torch.addcmul`
        """
        pass

    def addcmul_(self, value=1, tensor1, tensor2): # real signature unknown; restored from __doc__
        """
        addcmul_(value=1, tensor1, tensor2) -> Tensor
        
        In-place version of :meth:`~Tensor.addcmul`
        """
        pass

    def addmm(self, beta=1, mat, alpha=1, mat1, mat2): # real signature unknown; restored from __doc__
        """
        addmm(beta=1, mat, alpha=1, mat1, mat2) -> Tensor
        
        See :func:`torch.addmm`
        """
        pass

    def addmm_(self, beta=1, mat, alpha=1, mat1, mat2): # real signature unknown; restored from __doc__
        """
        addmm_(beta=1, mat, alpha=1, mat1, mat2) -> Tensor
        
        In-place version of :meth:`~Tensor.addmm`
        """
        pass

    def addmv(self, beta=1, tensor, alpha=1, mat, vec): # real signature unknown; restored from __doc__
        """
        addmv(beta=1, tensor, alpha=1, mat, vec) -> Tensor
        
        See :func:`torch.addmv`
        """
        pass

    def addmv_(self, beta=1, tensor, alpha=1, mat, vec): # real signature unknown; restored from __doc__
        """
        addmv_(beta=1, tensor, alpha=1, mat, vec) -> Tensor
        
        In-place version of :meth:`~Tensor.addmv`
        """
        pass

    def addr(self, beta=1, alpha=1, vec1, vec2): # real signature unknown; restored from __doc__
        """
        addr(beta=1, alpha=1, vec1, vec2) -> Tensor
        
        See :func:`torch.addr`
        """
        pass

    def addr_(self, beta=1, alpha=1, vec1, vec2): # real signature unknown; restored from __doc__
        """
        addr_(beta=1, alpha=1, vec1, vec2) -> Tensor
        
        In-place version of :meth:`~Tensor.addr`
        """
        pass

    def add_(self, value): # real signature unknown; restored from __doc__
        """
        add_(value)
        
        In-place version of :meth:`~Tensor.add`
        """
        pass

    def apply_(self, callable): # real signature unknown; restored from __doc__
        """
        apply_(callable) -> Tensor
        
        Applies the function :attr:`callable` to each element in the tensor, replacing
        each element with the value returned by :attr:`callable`.
        
        .. note::
        
            This function only works with CPU tensors and should not be used in code
            sections that require high performance.
        """
        pass

    def asin(self): # real signature unknown; restored from __doc__
        """
        asin() -> Tensor
        
        See :func:`torch.asin`
        """
        pass

    def asin_(self): # real signature unknown; restored from __doc__
        """
        asin_() -> Tensor
        
        In-place version of :meth:`~Tensor.asin`
        """
        pass

    def atan(self): # real signature unknown; restored from __doc__
        """
        atan() -> Tensor
        
        See :func:`torch.atan`
        """
        pass

    def atan2(self, other): # real signature unknown; restored from __doc__
        """
        atan2(other) -> Tensor
        
        See :func:`torch.atan2`
        """
        pass

    def atan2_(self, other): # real signature unknown; restored from __doc__
        """
        atan2_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.atan2`
        """
        pass

    def atan_(self): # real signature unknown; restored from __doc__
        """
        atan_() -> Tensor
        
        In-place version of :meth:`~Tensor.atan`
        """
        pass

    def baddbmm(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        baddbmm(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        See :func:`torch.baddbmm`
        """
        pass

    def baddbmm_(self, beta=1, alpha=1, batch1, batch2): # real signature unknown; restored from __doc__
        """
        baddbmm_(beta=1, alpha=1, batch1, batch2) -> Tensor
        
        In-place version of :meth:`~Tensor.baddbmm`
        """
        pass

    def bernoulli(self): # real signature unknown; restored from __doc__
        """
        bernoulli() -> Tensor
        
        See :func:`torch.bernoulli`
        """
        pass

    def bernoulli_(self): # real signature unknown; restored from __doc__
        """
        bernoulli_() -> Tensor
        
        In-place version of :meth:`~Tensor.bernoulli`
        """
        pass

    def bmm(self, batch2): # real signature unknown; restored from __doc__
        """
        bmm(batch2) -> Tensor
        
        See :func:`torch.bmm`
        """
        pass

    def btrifact(self, *args, **kwargs): # real signature unknown
        pass

    def btrisolve(self, *args, **kwargs): # real signature unknown
        pass

    def cauchy_(self, median=0, sigma=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        cauchy_(median=0, sigma=1, *, generator=None) -> Tensor
        
        Fills the tensor with numbers drawn from the Cauchy distribution:
        
        .. math::
        
            P(x) = \dfrac{1}{\pi} \dfrac{\sigma}{(x - median)^2 + \sigma^2}
        """
        pass

    def ceil(self): # real signature unknown; restored from __doc__
        """
        ceil() -> Tensor
        
        See :func:`torch.ceil`
        """
        pass

    def ceil_(self): # real signature unknown; restored from __doc__
        """
        ceil_() -> Tensor
        
        In-place version of :meth:`~Tensor.ceil`
        """
        pass

    def clamp(self, min, max): # real signature unknown; restored from __doc__
        """
        clamp(min, max) -> Tensor
        
        See :func:`torch.clamp`
        """
        pass

    def clamp_(self, min, max): # real signature unknown; restored from __doc__
        """
        clamp_(min, max) -> Tensor
        
        In-place version of :meth:`~Tensor.clamp`
        """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """
        clone() -> Tensor
        
        Returns a copy of the tensor. The copy has the same size and data type as the
        original tensor.
        """
        pass

    def contiguous(self): # real signature unknown; restored from __doc__
        """
        contiguous() -> Tensor
        
        Returns a contiguous Tensor containing the same data as this tensor. If this
        tensor is contiguous, this function returns the original tensor.
        """
        pass

    def copy_(self, src, async=False): # real signature unknown; restored from __doc__
        """
        copy_(src, async=False) -> Tensor
        
        Copies the elements from :attr:`src` into this tensor and returns this tensor.
        
        The source tensor should have the same number of elements as this tensor. It
        may be of a different data type or reside on a different device.
        
        Args:
            src (Tensor): Source tensor to copy
            async (bool): If True and this copy is between CPU and GPU, then the copy
                          may occur asynchronously with respect to the host. For other
                          copies, this argument has no effect.
        """
        pass

    def cos(self): # real signature unknown; restored from __doc__
        """
        cos() -> Tensor
        
        See :func:`torch.cos`
        """
        pass

    def cosh(self): # real signature unknown; restored from __doc__
        """
        cosh() -> Tensor
        
        See :func:`torch.cosh`
        """
        pass

    def cosh_(self): # real signature unknown; restored from __doc__
        """
        cosh_() -> Tensor
        
        In-place version of :meth:`~Tensor.cosh`
        """
        pass

    def cos_(self): # real signature unknown; restored from __doc__
        """
        cos_() -> Tensor
        
        In-place version of :meth:`~Tensor.cos`
        """
        pass

    def cross(self, other, dim=-1): # real signature unknown; restored from __doc__
        """
        cross(other, dim=-1) -> Tensor
        
        See :func:`torch.cross`
        """
        pass

    def cumprod(self, dim): # real signature unknown; restored from __doc__
        """
        cumprod(dim) -> Tensor
        
        See :func:`torch.cumprod`
        """
        pass

    def cumsum(self, dim): # real signature unknown; restored from __doc__
        """
        cumsum(dim) -> Tensor
        
        See :func:`torch.cumsum`
        """
        pass

    def data_ptr(self): # real signature unknown; restored from __doc__
        """
        data_ptr() -> int
        
        Returns the address of the first element of this tensor.
        """
        return 0

    def diag(self, diagonal=0): # real signature unknown; restored from __doc__
        """
        diag(diagonal=0) -> Tensor
        
        See :func:`torch.diag`
        """
        pass

    def dim(self): # real signature unknown; restored from __doc__
        """
        dim() -> int
        
        Returns the number of dimensions of this tensor.
        """
        return 0

    def dist(self, other, p=2): # real signature unknown; restored from __doc__
        """
        dist(other, p=2) -> Tensor
        
        See :func:`torch.dist`
        """
        pass

    def div(self, value): # real signature unknown; restored from __doc__
        """
        div(value)
        
        See :func:`torch.div`
        """
        pass

    def div_(self, value): # real signature unknown; restored from __doc__
        """
        div_(value)
        
        In-place version of :meth:`~Tensor.div`
        """
        pass

    def dot(self, tensor2): # real signature unknown; restored from __doc__
        """
        dot(tensor2) -> float
        
        See :func:`torch.dot`
        """
        return 0.0

    def eig(self, eigenvectors=False): # real signature unknown; restored from __doc__
        """
        eig(eigenvectors=False) -> (Tensor, Tensor)
        
        See :func:`torch.eig`
        """
        pass

    def element_size(self): # real signature unknown; restored from __doc__
        """
        element_size() -> int
        
        Returns the size in bytes of an individual element.
        
        Example:
            >>> torch.FloatTensor().element_size()
            4
            >>> torch.ByteTensor().element_size()
            1
        """
        return 0

    def eq(self, other): # real signature unknown; restored from __doc__
        """
        eq(other) -> Tensor
        
        See :func:`torch.eq`
        """
        pass

    def equal(self, other): # real signature unknown; restored from __doc__
        """
        equal(other) -> bool
        
        See :func:`torch.equal`
        """
        return False

    def eq_(self, other): # real signature unknown; restored from __doc__
        """
        eq_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.eq`
        """
        pass

    def exp(self): # real signature unknown; restored from __doc__
        """
        exp() -> Tensor
        
        See :func:`torch.exp`
        """
        pass

    def expand(self, tensor, sizes): # real signature unknown; restored from __doc__
        """
        expand(tensor, sizes) -> Tensor
        
        Returns a new view of the tensor with singleton dimensions expanded
        to a larger size.
        
        Tensor can be also expanded to a larger number of dimensions, and the
        new ones will be appended at the front.
        
        Expanding a tensor does not allocate new memory, but only creates a
        new view on the existing tensor where a dimension of size one is
        expanded to a larger size by setting the ``stride`` to 0. Any dimension
        of size 1 can be expanded to an arbitrary value without allocating new
        memory.
        
        Args:
            *sizes (torch.Size or int...): The desired expanded size
        
        Example:
            >>> x = torch.Tensor([[1], [2], [3]])
            >>> x.size()
            torch.Size([3, 1])
            >>> x.expand(3, 4)
             1  1  1  1
             2  2  2  2
             3  3  3  3
            [torch.FloatTensor of size 3x4]
        """
        pass

    def exponential_(self, lambd=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        exponential_(lambd=1, *, generator=None) -> Tensor
        
        Fills this tensor with elements drawn from the exponential distribution:
        
        .. math::
        
            P(x) = \lambda e^{-\lambda x}
        """
        pass

    def exp_(self): # real signature unknown; restored from __doc__
        """
        exp_() -> Tensor
        
        In-place version of :meth:`~Tensor.exp`
        """
        pass

    def fill_(self, value): # real signature unknown; restored from __doc__
        """
        fill_(value) -> Tensor
        
        Fills this tensor with the specified value.
        """
        pass

    def floor(self): # real signature unknown; restored from __doc__
        """
        floor() -> Tensor
        
        See :func:`torch.floor`
        """
        pass

    def floor_(self): # real signature unknown; restored from __doc__
        """
        floor_() -> Tensor
        
        In-place version of :meth:`~Tensor.floor`
        """
        pass

    def fmod(self, divisor): # real signature unknown; restored from __doc__
        """
        fmod(divisor) -> Tensor
        
        See :func:`torch.fmod`
        """
        pass

    def fmod_(self, divisor): # real signature unknown; restored from __doc__
        """
        fmod_(divisor) -> Tensor
        
        In-place version of :meth:`~Tensor.fmod`
        """
        pass

    def frac(self): # real signature unknown; restored from __doc__
        """
        frac() -> Tensor
        
        See :func:`torch.frac`
        """
        pass

    def frac_(self): # real signature unknown; restored from __doc__
        """
        frac_() -> Tensor
        
        In-place version of :meth:`~Tensor.frac`
        """
        pass

    def gather(self, dim, index): # real signature unknown; restored from __doc__
        """
        gather(dim, index) -> Tensor
        
        See :func:`torch.gather`
        """
        pass

    def ge(self, other): # real signature unknown; restored from __doc__
        """
        ge(other) -> Tensor
        
        See :func:`torch.ge`
        """
        pass

    def gels(self, A): # real signature unknown; restored from __doc__
        """
        gels(A) -> Tensor
        
        See :func:`torch.gels`
        """
        pass

    def geometric_(self, p, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        geometric_(p, *, generator=None) -> Tensor
        
        Fills this tensor with elements drawn from the geometric distribution:
        
        .. math::
        
            P(X=k) = (1 - p)^{k - 1} p
        """
        pass

    def geqrf(self): # real signature unknown; restored from __doc__
        """
        geqrf() -> (Tensor, Tensor)
        
        See :func:`torch.geqrf`
        """
        pass

    def ger(self, vec2): # real signature unknown; restored from __doc__
        """
        ger(vec2) -> Tensor
        
        See :func:`torch.ger`
        """
        pass

    def gesv(self, A): # real signature unknown; restored from __doc__
        """
        gesv(A) -> Tensor, Tensor
        
        See :func:`torch.gesv`
        """
        pass

    def ge_(self, other): # real signature unknown; restored from __doc__
        """
        ge_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.ge`
        """
        pass

    def gt(self, other): # real signature unknown; restored from __doc__
        """
        gt(other) -> Tensor
        
        See :func:`torch.gt`
        """
        pass

    def gt_(self, other): # real signature unknown; restored from __doc__
        """
        gt_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.gt`
        """
        pass

    def histc(self, bins=100, min=0, max=0): # real signature unknown; restored from __doc__
        """
        histc(bins=100, min=0, max=0) -> Tensor
        
        See :func:`torch.histc`
        """
        pass

    def index(self, m): # real signature unknown; restored from __doc__
        """
        index(m) -> Tensor
        
        Selects elements from this tensor using a binary mask or along a given
        dimension. The expression ``tensor.index(m)`` is equivalent to ``tensor[m]``.
        
        Args:
            m (int or ByteTensor or slice): The dimension or mask used to select elements
        """
        pass

    def index_add_(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_add_(dim, index, tensor) -> Tensor
        
        Accumulate the elements of tensor into the original tensor by adding to the
        indices in the order given in index. The shape of tensor must exactly match the
        elements indexed or an error will be raised.
        
        Args:
            dim (int): Dimension along which to index
            index (LongTensor): Indices to select from tensor
            tensor (Tensor): Tensor containing values to add
        
        Example:
            >>> x = torch.Tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
            >>> t = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> index = torch.LongTensor([0, 2, 1])
            >>> x.index_add_(0, index, t)
            >>> x
              2   3   4
              8   9  10
              5   6   7
            [torch.FloatTensor of size 3x3]
        """
        pass

    def index_copy_(self, dim, index, tensor): # real signature unknown; restored from __doc__
        """
        index_copy_(dim, index, tensor) -> Tensor
        
        Copies the elements of tensor into the original tensor by selecting the
        indices in the order given in index. The shape of tensor must exactly match the
        elements indexed or an error will be raised.
        
        Args:
            dim (int): Dimension along which to index
            index (LongTensor): Indices to select from tensor
            tensor (Tensor): Tensor containing values to copy
        
        Example:
            >>> x = torch.Tensor(3, 3)
            >>> t = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> index = torch.LongTensor([0, 2, 1])
            >>> x.index_copy_(0, index, t)
            >>> x
             1  2  3
             7  8  9
             4  5  6
            [torch.FloatTensor of size 3x3]
        """
        pass

    def index_fill_(self, dim, index, val): # real signature unknown; restored from __doc__
        """
        index_fill_(dim, index, val) -> Tensor
        
        Fills the elements of the original tensor with value :attr:`val` by selecting
        the indices in the order given in index.
        
        Args:
            dim (int): Dimension along which to index
            index (LongTensor): Indices
            val (float): Value to fill
        
        Example:
            >>> x = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> index = torch.LongTensor([0, 2])
            >>> x.index_fill_(1, index, -1)
            >>> x
            -1  2 -1
            -1  5 -1
            -1  8 -1
            [torch.FloatTensor of size 3x3]
        """
        pass

    def index_select(self, dim, index): # real signature unknown; restored from __doc__
        """
        index_select(dim, index) -> Tensor
        
        See :func:`torch.index_select`
        """
        pass

    def inverse(self): # real signature unknown; restored from __doc__
        """
        inverse() -> Tensor
        
        See :func:`torch.inverse`
        """
        pass

    def is_contiguous(self): # real signature unknown; restored from __doc__
        """
        is_contiguous() -> bool
        
        Returns True if this tensor is contiguous in memory in C order.
        """
        return False

    def is_same_size(self, *args, **kwargs): # real signature unknown
        pass

    def is_set_to(self, tensor): # real signature unknown; restored from __doc__
        """
        is_set_to(tensor) -> bool
        
        Returns True if this object refers to the same ``THTensor`` object from the
        Torch C API as the given tensor.
        """
        return False

    def kthvalue(self, k, dim=None): # real signature unknown; restored from __doc__
        """
        kthvalue(k, dim=None) -> (Tensor, LongTensor)
        
        See :func:`torch.kthvalue`
        """
        pass

    def le(self, other): # real signature unknown; restored from __doc__
        """
        le(other) -> Tensor
        
        See :func:`torch.le`
        """
        pass

    def lerp(self, start, end, weight): # real signature unknown; restored from __doc__
        """
        lerp(start, end, weight)
        
        See :func:`torch.lerp`
        """
        pass

    def lerp_(self, start, end, weight): # real signature unknown; restored from __doc__
        """
        lerp_(start, end, weight)
        
        In-place version of :meth:`~Tensor.lerp`
        """
        pass

    def le_(self, other): # real signature unknown; restored from __doc__
        """
        le_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.le`
        """
        pass

    def log(self): # real signature unknown; restored from __doc__
        """
        log() -> Tensor
        
        See :func:`torch.log`
        """
        pass

    def log1p(self): # real signature unknown; restored from __doc__
        """
        log1p() -> Tensor
        
        See :func:`torch.log1p`
        """
        pass

    def log1p_(self): # real signature unknown; restored from __doc__
        """
        log1p_() -> Tensor
        
        In-place version of :meth:`~Tensor.log1p`
        """
        pass

    def log_(self): # real signature unknown; restored from __doc__
        """
        log_() -> Tensor
        
        In-place version of :meth:`~Tensor.log`
        """
        pass

    def log_normal_(self, mean=1, std=2, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        log_normal_(mean=1, std=2, *, generator=None)
        
        Fills this tensor with numbers samples from the log-normal distribution
        parameterized by the given mean (µ) and standard deviation (σ). Note that
        :attr:`mean` and :attr:`stdv` are the mean and standard deviation of the
        underlying normal distribution, and not of the returned distribution:
        
        .. math::
        
            P(x) = \dfrac{1}{x \sigma \sqrt{2\pi}} e^{-\dfrac{(\ln x - \mu)^2}{2\sigma^2}}
        """
        pass

    def lt(self, other): # real signature unknown; restored from __doc__
        """
        lt(other) -> Tensor
        
        See :func:`torch.lt`
        """
        pass

    def lt_(self, other): # real signature unknown; restored from __doc__
        """
        lt_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.lt`
        """
        pass

    def map2_(self, *args, **kwargs): # real signature unknown
        pass

    def map_(self, tensor, callable): # real signature unknown; restored from __doc__
        """
        map_(tensor, callable)
        
        Applies :attr:`callable` for each element in this tensor and the given tensor
        and stores the results in this tensor. The :attr:`callable` should have the
        signature::
        
            def callable(a, b) -> number
        """
        pass

    def masked_copy_(self, mask, source): # real signature unknown; restored from __doc__
        """
        masked_copy_(mask, source)
        
        Copies elements from :attr:`source` into this tensor at positions where the
        :attr:`mask` is one. The :attr:`mask` should have the same number of elements
        as this tensor. The :attr:`source` should have at least as many elements as the
        number of ones in :attr:`mask`
        
        Args:
            mask (ByteTensor): The binary mask
            source (Tensor): The tensor to copy from
        
        .. note::
        
            The :attr:`mask` operates on the :attr:`self` tensor, not on the given
            :attr:`source` tensor.
        """
        pass

    def masked_fill_(self, mask, value): # real signature unknown; restored from __doc__
        """
        masked_fill_(mask, value)
        
        Fills elements of this tensor with :attr:`value` where :attr:`mask` is one.
        The :attr:`mask` should have the same number of elements as this tensor, but
        the shape may differ.
        
        Args:
            mask (ByteTensor): The binary mask
            value (Tensor): The value to fill
        """
        pass

    def masked_select(self, mask): # real signature unknown; restored from __doc__
        """
        masked_select(mask) -> Tensor
        
        See :func:`torch.masked_select`
        """
        pass

    def max(self, dim=None): # real signature unknown; restored from __doc__
        """
        max(dim=None) -> float or (Tensor, Tensor)
        
        See :func:`torch.max`
        """
        return 0.0

    def mean(self, dim=None): # real signature unknown; restored from __doc__
        """
        mean(dim=None) -> float or (Tensor, Tensor)
        
        See :func:`torch.mean`
        """
        return 0.0

    def median(self, dim=-1, values=None, indices=None): # real signature unknown; restored from __doc__
        """
        median(dim=-1, values=None, indices=None) -> (Tensor, LongTensor)
        
        See :func:`torch.median`
        """
        pass

    def min(self, dim=None): # real signature unknown; restored from __doc__
        """
        min(dim=None) -> float or (Tensor, Tensor)
        
        See :func:`torch.min`
        """
        return 0.0

    def mm(self, mat2): # real signature unknown; restored from __doc__
        """
        mm(mat2) -> Tensor
        
        See :func:`torch.mm`
        """
        pass

    def mode(self, dim=-1, values=None, indices=None): # real signature unknown; restored from __doc__
        """
        mode(dim=-1, values=None, indices=None) -> (Tensor, LongTensor)
        
        See :func:`torch.mode`
        """
        pass

    def mul(self, value): # real signature unknown; restored from __doc__
        """
        mul(value) -> Tensor
        
        See :func:`torch.mul`
        """
        pass

    def multinomial(self, num_samples, replacement=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        multinomial(num_samples, replacement=False, *, generator=None)
        
        See :func:`torch.multinomial`
        """
        pass

    def mul_(self, value): # real signature unknown; restored from __doc__
        """
        mul_(value)
        
        In-place version of :meth:`~Tensor.mul`
        """
        pass

    def mv(self, vec): # real signature unknown; restored from __doc__
        """
        mv(vec) -> Tensor
        
        See :func:`torch.mv`
        """
        pass

    def narrow(self, dimension, start, length): # real signature unknown; restored from __doc__
        """
        narrow(dimension, start, length) -> Tensor
        
        Returns a new tensor that is a narrowed version of this tensor. The dimension
        :attr:`dim` is narrowed from :attr:`start` to :attr:`start + length`. The
        returned tensor and this tensor share the same underlying storage.
        
        Args:
            dimension (int): The dimension along which to narrow
            start (int): The starting dimension
            length (int):
        
        Example:
            >>> x = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> x.narrow(0, 0, 2)
             1  2  3
             4  5  6
            [torch.FloatTensor of size 2x3]
            >>> x.narrow(1, 1, 2)
             2  3
             5  6
             8  9
            [torch.FloatTensor of size 3x2]
        """
        pass

    def ndimension(self): # real signature unknown; restored from __doc__
        """
        ndimension() -> int
        
        Alias for :meth:`~Tensor.dim()`
        """
        return 0

    def ne(self, other): # real signature unknown; restored from __doc__
        """
        ne(other) -> Tensor
        
        See :func:`torch.ne`
        """
        pass

    def neg(self): # real signature unknown; restored from __doc__
        """
        neg() -> Tensor
        
        See :func:`torch.neg`
        """
        pass

    def neg_(self): # real signature unknown; restored from __doc__
        """
        neg_() -> Tensor
        
        In-place version of :meth:`~Tensor.neg`
        """
        pass

    def nelement(self): # real signature unknown; restored from __doc__
        """
        nelement() -> int
        
        Alias for :meth:`~Tensor.numel`
        """
        return 0

    def ne_(self, other): # real signature unknown; restored from __doc__
        """
        ne_(other) -> Tensor
        
        In-place version of :meth:`~Tensor.ne`
        """
        pass

    def nonzero(self): # real signature unknown; restored from __doc__
        """
        nonzero() -> LongTensor
        
        See :func:`torch.nonzero`
        """
        pass

    def norm(self, p=2): # real signature unknown; restored from __doc__
        """
        norm(p=2) -> float
        
        See :func:`torch.norm`
        """
        return 0.0

    def normal_(self, mean=0, std=1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        normal_(mean=0, std=1, *, generator=None)
        
        Fills this tensor with elements samples from the normal distribution
        parameterized by :attr:`mean` and :attr:`std`.
        """
        pass

    def numel(self): # real signature unknown; restored from __doc__
        """
        numel() -> int
        
        See :func:`torch.numel`
        """
        return 0

    def numpy(self): # real signature unknown; restored from __doc__
        """
        numpy() -> ndarray
        
        Returns this tensor as a NumPy :class:`ndarray`. This tensor and the returned
        :class:`ndarray` share the same underlying storage. Changes to this tensor will
        be reflected in the :class:`ndarray` and vice versa.
        """
        pass

    def orgqr(self, input2): # real signature unknown; restored from __doc__
        """
        orgqr(input2) -> Tensor
        
        See :func:`torch.orgqr`
        """
        pass

    def ormqr(self, input2, input3, left=True, transpose=False): # real signature unknown; restored from __doc__
        """
        ormqr(input2, input3, left=True, transpose=False) -> Tensor
        
        See :func:`torch.ormqr`
        """
        pass

    def potrf(self, upper=True): # real signature unknown; restored from __doc__
        """
        potrf(upper=True) -> Tensor
        
        See :func:`torch.potrf`
        """
        pass

    def potri(self, upper=True): # real signature unknown; restored from __doc__
        """
        potri(upper=True) -> Tensor
        
        See :func:`torch.potri`
        """
        pass

    def potrs(self, input2, upper=True): # real signature unknown; restored from __doc__
        """
        potrs(input2, upper=True) -> Tensor
        
        See :func:`torch.potrs`
        """
        pass

    def pow(self, exponent): # real signature unknown; restored from __doc__
        """
        pow(exponent)
        
        See :func:`torch.pow`
        """
        pass

    def pow_(self, exponent): # real signature unknown; restored from __doc__
        """
        pow_(exponent)
        
        In-place version of :meth:`~Tensor.pow`
        """
        pass

    def prod(self): # real signature unknown; restored from __doc__
        """
        prod() -> float
        
        See :func:`torch.prod`
        """
        return 0.0

    def pstrf(self, upper=True, tol=-1): # real signature unknown; restored from __doc__
        """
        pstrf(upper=True, tol=-1) -> (Tensor, IntTensor)
        
        See :func:`torch.pstrf`
        """
        pass

    def qr(self): # real signature unknown; restored from __doc__
        """
        qr() -> (Tensor, Tensor)
        
        See :func:`torch.qr`
        """
        pass

    def random_(self, from=0, to=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        random_(from=0, to=None, *, generator=None)
        
        Fills this tensor with numbers sampled from the uniform distribution or
        discrete uniform distribution over [from, to - 1]. If not specified, the
        values are only bounded by this tensor's data type.
        """
        pass

    def reciprocal(self): # real signature unknown; restored from __doc__
        """
        reciprocal() -> Tensor
        
        See :func:`torch.reciprocal`
        """
        pass

    def reciprocal_(self): # real signature unknown; restored from __doc__
        """
        reciprocal_() -> Tensor
        
        In-place version of :meth:`~Tensor.reciprocal`
        """
        pass

    def remainder(self, divisor): # real signature unknown; restored from __doc__
        """
        remainder(divisor) -> Tensor
        
        See :func:`torch.remainder`
        """
        pass

    def remainder_(self, divisor): # real signature unknown; restored from __doc__
        """
        remainder_(divisor) -> Tensor
        
        In-place version of :meth:`~Tensor.remainder`
        """
        pass

    def renorm(self, p, dim, maxnorm): # real signature unknown; restored from __doc__
        """
        renorm(p, dim, maxnorm) -> Tensor
        
        See :func:`torch.renorm`
        """
        pass

    def renorm_(self, p, dim, maxnorm): # real signature unknown; restored from __doc__
        """
        renorm_(p, dim, maxnorm) -> Tensor
        
        In-place version of :meth:`~Tensor.renorm`
        """
        pass

    def resize_(self, *sizes): # real signature unknown; restored from __doc__
        """
        resize_(*sizes)
        
        Resizes this tensor to the specified size. If the number of elements is
        larger than the current storage size, then the underlying storage is resized
        to fit the new number of elements. If the number of elements is smaller, the
        underlying storage is not changed. Existing elements are preserved but any new
        memory is uninitialized.
        
        Args:
            sizes (torch.Size or int...): The desired size
        
        Example:
            >>> x = torch.Tensor([[1, 2], [3, 4], [5, 6]])
            >>> x.resize_(2, 2)
            >>> x
             1  2
             3  4
            [torch.FloatTensor of size 2x2]
        """
        pass

    def resize_as_(self, tensor): # real signature unknown; restored from __doc__
        """
        resize_as_(tensor)
        
        Resizes the current tensor to be the same size as the specified tensor. This is
        equivalent to::
        
            self.resize_(tensor.size())
        """
        pass

    def round(self): # real signature unknown; restored from __doc__
        """
        round() -> Tensor
        
        See :func:`torch.round`
        """
        pass

    def round_(self): # real signature unknown; restored from __doc__
        """
        round_() -> Tensor
        
        In-place version of :meth:`~Tensor.round`
        """
        pass

    def rsqrt(self): # real signature unknown; restored from __doc__
        """
        rsqrt() -> Tensor
        
        See :func:`torch.rsqrt`
        """
        pass

    def rsqrt_(self): # real signature unknown; restored from __doc__
        """
        rsqrt_() -> Tensor
        
        In-place version of :meth:`~Tensor.rsqrt`
        """
        pass

    def scatter_(self, input, dim, index, src): # real signature unknown; restored from __doc__
        """
        scatter_(input, dim, index, src) -> Tensor
        
        Writes all values from the Tensor :attr:`src` into self at the indices specified
        in the :attr:`index` Tensor. The indices are specified with respect to the
        given dimension, dim, in the manner described in :meth:`~Tensor.gather`.
        
        Note that, as for gather, the values of index must be between `0` and `(self.size(dim) -1)`
        inclusive and all values in a row along the specified dimension must be unique.
        
        Args:
            input (Tensor): The source tensor
            dim (int): The axis along which to index
            index (LongTensor): The indices of elements to scatter
            src (Tensor or float): The source element(s) to scatter
        
        Example::
        
            >>> x = torch.rand(2, 5)
            >>> x
        
             0.4319  0.6500  0.4080  0.8760  0.2355
             0.2609  0.4711  0.8486  0.8573  0.1029
            [torch.FloatTensor of size 2x5]
        
            >>> torch.zeros(3, 5).scatter_(0, torch.LongTensor([[0, 1, 2, 0, 0], [2, 0, 0, 1, 2]]), x)
        
             0.4319  0.4711  0.8486  0.8760  0.2355
             0.0000  0.6500  0.0000  0.8573  0.0000
             0.2609  0.0000  0.4080  0.0000  0.1029
            [torch.FloatTensor of size 3x5]
        
            >>> z = torch.zeros(2, 4).scatter_(1, torch.LongTensor([[2], [3]]), 1.23)
            >>> z
        
             0.0000  0.0000  1.2300  0.0000
             0.0000  0.0000  0.0000  1.2300
            [torch.FloatTensor of size 2x4]
        """
        pass

    def select(self, dim, index): # real signature unknown; restored from __doc__
        """
        select(dim, index) -> Tensor or number
        
        Slices the tensor along the selected dimension at the given index. If this
        tensor is one dimensional, this function returns a number. Otherwise, it
        returns a tensor with the given dimension removed.
        
        Args:
            dim (int): Dimension to slice
            index (int): Index to select
        
        .. note::
        
            :meth:`select` is equivalent to slicing. For example, ``tensor.select(0, index)``
            is equivalent to ``tensor[index]`` and ``tensor.select(2, index)`` is equivalent
            to ``tensor[:,:,index]``.
        """
        pass

    def set_(self, source=None, storage_offset=0, size=None, stride=None): # real signature unknown; restored from __doc__
        """
        set_(source=None, storage_offset=0, size=None, stride=None)
        
        Sets the underlying storage, size, and strides. If :attr:`source` is a tensor,
        this tensor will share the same storage and have the same size and strides
        as the given tensor. Changes to elements in one tensor will be reflected in the
        other.
        
        If :attr:`source` is a :class:`~torch.Storage`, the method sets the underlying
        storage, offset, size, and stride.
        
        Args:
            source (Tensor or Storage): The tensor or storage to use
            storage_offset (int): The offset in the storage
            size (torch.Size): The desired size. Defaults to the size of the source.
            stride (tuple): The desired stride. Defaults to C-contiguous strides.
        """
        pass

    def sigmoid(self): # real signature unknown; restored from __doc__
        """
        sigmoid() -> Tensor
        
        See :func:`torch.sigmoid`
        """
        pass

    def sigmoid_(self): # real signature unknown; restored from __doc__
        """
        sigmoid_() -> Tensor
        
        In-place version of :meth:`~Tensor.sigmoid`
        """
        pass

    def sign(self): # real signature unknown; restored from __doc__
        """
        sign() -> Tensor
        
        See :func:`torch.sign`
        """
        pass

    def sign_(self): # real signature unknown; restored from __doc__
        """
        sign_() -> Tensor
        
        In-place version of :meth:`~Tensor.sign`
        """
        pass

    def sin(self): # real signature unknown; restored from __doc__
        """
        sin() -> Tensor
        
        See :func:`torch.sin`
        """
        pass

    def sinh(self): # real signature unknown; restored from __doc__
        """
        sinh() -> Tensor
        
        See :func:`torch.sinh`
        """
        pass

    def sinh_(self): # real signature unknown; restored from __doc__
        """
        sinh_() -> Tensor
        
        In-place version of :meth:`~Tensor.sinh`
        """
        pass

    def sin_(self): # real signature unknown; restored from __doc__
        """
        sin_() -> Tensor
        
        In-place version of :meth:`~Tensor.sin`
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        size() -> torch.Size
        
        Returns the size of the tensor. The returned value is a subclass of
        :class:`tuple`.
        
        Example:
            >>> torch.Tensor(3, 4, 5).size()
            torch.Size([3, 4, 5])
        """
        pass

    def sort(self, dim=None, descending=False): # real signature unknown; restored from __doc__
        """
        sort(dim=None, descending=False) -> (Tensor, LongTensor)
        
        See :func:`torch.sort`
        """
        pass

    def sparse_mask(self, *args, **kwargs): # real signature unknown
        pass

    def sqrt(self): # real signature unknown; restored from __doc__
        """
        sqrt() -> Tensor
        
        See :func:`torch.sqrt`
        """
        pass

    def sqrt_(self): # real signature unknown; restored from __doc__
        """
        sqrt_() -> Tensor
        
        In-place version of :meth:`~Tensor.sqrt`
        """
        pass

    def squeeze(self, dim=None): # real signature unknown; restored from __doc__
        """
        squeeze(dim=None)
        
        See :func:`torch.squeeze`
        """
        pass

    def squeeze_(self, dim=None): # real signature unknown; restored from __doc__
        """
        squeeze_(dim=None)
        
        In-place version of :meth:`~Tensor.squeeze`
        """
        pass

    def std(self): # real signature unknown; restored from __doc__
        """
        std() -> float
        
        See :func:`torch.std`
        """
        return 0.0

    def storage(self): # real signature unknown; restored from __doc__
        """
        storage() -> torch.Storage
        
        Returns the underlying storage
        """
        pass

    def storage_offset(self): # real signature unknown; restored from __doc__
        """
        storage_offset() -> int
        
        Returns this tensor's offset in the underlying storage in terms of number of
        storage elements (not bytes).
        
        Example:
            >>> x = torch.Tensor([1, 2, 3, 4, 5])
            >>> x.storage_offset()
            0
            >>> x[3:].storage_offset()
            3
        """
        return 0

    def stride(self): # real signature unknown; restored from __doc__
        """
        stride() -> tuple
        
        Returns the stride of the tensor.
        """
        return ()

    def sub(self, value, other): # real signature unknown; restored from __doc__
        """
        sub(value, other) -> Tensor
        
        Subtracts a scalar or tensor from this tensor. If both :attr:`value` and
        :attr:`other` are specified, each element of :attr:`other` is scaled by
        :attr:`value` before being used.
        """
        pass

    def sub_(self, x): # real signature unknown; restored from __doc__
        """
        sub_(x) -> Tensor
        
        In-place version of :meth:`~Tensor.sub`
        """
        pass

    def sum(self, dim=None): # real signature unknown; restored from __doc__
        """
        sum(dim=None) -> float
        
        See :func:`torch.sum`
        """
        return 0.0

    def svd(self, some=True): # real signature unknown; restored from __doc__
        """
        svd(some=True) -> (Tensor, Tensor, Tensor)
        
        See :func:`torch.svd`
        """
        pass

    def symeig(self, eigenvectors=False, upper=True): # real signature unknown; restored from __doc__
        """
        symeig(eigenvectors=False, upper=True) -> (Tensor, Tensor)
        
        See :func:`torch.symeig`
        """
        pass

    def t(self): # real signature unknown; restored from __doc__
        """
        t() -> Tensor
        
        See :func:`torch.t`
        """
        pass

    def tan(self): # real signature unknown; restored from __doc__
        """
        tan() -> Tensor
        
        See :func:`torch.tan`
        """
        pass

    def tanh(self): # real signature unknown; restored from __doc__
        """
        tanh() -> Tensor
        
        See :func:`torch.tanh`
        """
        pass

    def tanh_(self): # real signature unknown; restored from __doc__
        """
        tanh_() -> Tensor
        
        In-place version of :meth:`~Tensor.tanh`
        """
        pass

    def tan_(self): # real signature unknown; restored from __doc__
        """
        tan_() -> Tensor
        
        In-place version of :meth:`~Tensor.tan`
        """
        pass

    def topk(self, k, dim=None, largest=True, sorted=True): # real signature unknown; restored from __doc__
        """
        topk(k, dim=None, largest=True, sorted=True) -> (Tensor, LongTensor)
        
        See :func:`torch.topk`
        """
        pass

    def trace(self): # real signature unknown; restored from __doc__
        """
        trace() -> float
        
        See :func:`torch.trace`
        """
        return 0.0

    def transpose(self, dim0, dim1): # real signature unknown; restored from __doc__
        """
        transpose(dim0, dim1) -> Tensor
        
        See :func:`torch.transpose`
        """
        pass

    def transpose_(self, dim0, dim1): # real signature unknown; restored from __doc__
        """
        transpose_(dim0, dim1) -> Tensor
        
        In-place version of :meth:`~Tensor.transpose`
        """
        pass

    def tril(self, k=0): # real signature unknown; restored from __doc__
        """
        tril(k=0) -> Tensor
        
        See :func:`torch.tril`
        """
        pass

    def tril_(self, k=0): # real signature unknown; restored from __doc__
        """
        tril_(k=0) -> Tensor
        
        In-place version of :meth:`~Tensor.tril`
        """
        pass

    def triu(self, k=0): # real signature unknown; restored from __doc__
        """
        triu(k=0) -> Tensor
        
        See :func:`torch.triu`
        """
        pass

    def triu_(self, k=0): # real signature unknown; restored from __doc__
        """
        triu_(k=0) -> Tensor
        
        In-place version of :meth:`~Tensor.triu`
        """
        pass

    def trtrs(self, A, upper=True, transpose=False, unitriangular=False): # real signature unknown; restored from __doc__
        """
        trtrs(A, upper=True, transpose=False, unitriangular=False) -> (Tensor, Tensor)
        
        See :func:`torch.trtrs`
        """
        pass

    def trunc(self): # real signature unknown; restored from __doc__
        """
        trunc() -> Tensor
        
        See :func:`torch.trunc`
        """
        pass

    def trunc_(self): # real signature unknown; restored from __doc__
        """
        trunc_() -> Tensor
        
        In-place version of :meth:`~Tensor.trunc`
        """
        pass

    def t_(self): # real signature unknown; restored from __doc__
        """
        t_() -> Tensor
        
        In-place version of :meth:`~Tensor.t`
        """
        pass

    def unfold(self, dim, size, step): # real signature unknown; restored from __doc__
        """
        unfold(dim, size, step) -> Tensor
        
        Returns a tensor which contains all slices of size :attr:`size` in
        the dimension :attr:`dim`.
        
        Step between two slices is given by :attr:`step`.
        
        If `sizedim` is the original size of dimension dim, the size of dimension `dim`
        in the returned tensor will be `(sizedim - size) / step + 1`
        
        An additional dimension of size size is appended in the returned tensor.
        
        Args:
            dim (int): dimension in which unfolding happens
            size (int): size of each slice that is unfolded
            step (int): the step between each slice
        
        Example::
        
            >>> x = torch.arange(1, 8)
            >>> x
        
             1
             2
             3
             4
             5
             6
             7
            [torch.FloatTensor of size 7]
        
            >>> x.unfold(0, 2, 1)
        
             1  2
             2  3
             3  4
             4  5
             5  6
             6  7
            [torch.FloatTensor of size 6x2]
        
            >>> x.unfold(0, 2, 2)
        
             1  2
             3  4
             5  6
            [torch.FloatTensor of size 3x2]
        """
        pass

    def uniform_(self, from=0, to=1): # real signature unknown; restored from __doc__
        """
        uniform_(from=0, to=1) -> Tensor
        
        Fills this tensor with numbers sampled from the uniform distribution:
        
        .. math:
        
            P(x) = \dfrac{1}{to - from}
        """
        pass

    def unsqueeze(self, dim): # real signature unknown; restored from __doc__
        """
        unsqueeze(dim)
        
        See :func:`torch.unsqueeze`
        """
        pass

    def unsqueeze_(self, dim): # real signature unknown; restored from __doc__
        """
        unsqueeze_(dim)
        
        In-place version of :meth:`~Tensor.unsqueeze`
        """
        pass

    def var(self): # real signature unknown; restored from __doc__
        """
        var() -> float
        
        See :func:`torch.var`
        """
        return 0.0

    def view(self, *args): # real signature unknown; restored from __doc__
        """
        view(*args) -> Tensor
        
        Returns a new tensor with the same data but different size.
        
        The returned tensor shares the same data and must have the same number
        of elements, but may have a different size. A tensor must be
        :func:`contiguous` to be viewed.
        
        Args:
            args (torch.Size or int...): Desired size
        
        Example:
            >>> x = torch.randn(4, 4)
            >>> x.size()
            torch.Size([4, 4])
            >>> y = x.view(16)
            >>> y.size()
            torch.Size([16])
            >>> z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
            >>> z.size()
            torch.Size([2, 8])
        """
        pass

    def zero_(self): # real signature unknown; restored from __doc__
        """
        zero_()
        
        Fills this tensor with zeros.
        """
        pass

    def _new_with_metadata_file(self, *args, **kwargs): # real signature unknown
        pass

    def _set_index(self, *args, **kwargs): # real signature unknown
        pass

    def _write_metadata(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    _cdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



