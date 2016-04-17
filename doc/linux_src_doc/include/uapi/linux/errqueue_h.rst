.. -*- coding: utf-8; mode: rst -*-

==========
errqueue.h
==========


.. _`scm_timestamping`:

struct scm_timestamping
=======================

.. c:type:: scm_timestamping

    timestamps exposed through cmsg


.. _`scm_timestamping.definition`:

Definition
----------

.. code-block:: c

  struct scm_timestamping {
  };


.. _`scm_timestamping.members`:

Members
-------




.. _`scm_timestamping.description`:

Description
-----------


The timestamping interfaces SO_TIMESTAMPING, MSG_TSTAMP\_\*
communicate network timestamps by passing this struct in a cmsg with
:c:func:`recvmsg`. See Documentation/networking/timestamping.txt for details.

