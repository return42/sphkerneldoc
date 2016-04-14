.. -*- coding: utf-8; mode: rst -*-

==========
errqueue.h
==========

.. _`scm_timestamping`:

struct scm_timestamping
=======================

.. c:type:: struct scm_timestamping

    timestamps exposed through cmsg



Definition
----------

.. code-block:: c

  struct scm_timestamping {
  };



Members
-------



Description
-----------


The timestamping interfaces SO_TIMESTAMPING, MSG_TSTAMP_*
communicate network timestamps by passing this struct in a cmsg with
:c:func:`recvmsg`. See Documentation/networking/timestamping.txt for details.

