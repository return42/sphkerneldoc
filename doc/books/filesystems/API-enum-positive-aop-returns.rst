
.. _API-enum-positive-aop-returns:

=========================
enum positive_aop_returns
=========================

*man enum positive_aop_returns(9)*

*4.6.0-rc1*

aop return codes with specific semantics


Synopsis
========

.. code-block:: c

    enum positive_aop_returns {
      AOP_WRITEPAGE_ACTIVATE,
      AOP_TRUNCATED_PAGE
    };


Constants
=========

AOP_WRITEPAGE_ACTIVATE
    Informs the caller that page writeback has completed, that the page is still locked, and should be considered active. The VM uses this hint to return the page to the active
    list -- it won't be a candidate for writeback again in the near future. Other callers must be careful to unlock the page if they get this return. Returned by ``writepage``;

AOP_TRUNCATED_PAGE
    The AOP method that was handed a locked page has unlocked it and the page might have been truncated. The caller should back up to acquiring a new page and trying again. The aop
    will be taking reasonable precautions not to livelock. If the caller held a page reference, it should drop it before retrying. Returned by ``readpage``.


Description
===========

address_space_operation functions return these large constants to indicate special semantics to the caller. These are much larger than the bytes in a page to allow for functions
that return the number of bytes operated on in a given page.
