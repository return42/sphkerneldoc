.. -*- coding: utf-8; mode: rst -*-

=======
atalk.h
=======


.. _`atalk_iface`:

struct atalk_iface
==================

.. c:type:: atalk_iface

    AppleTalk Interface @dev - Network device associated with this interface @address - Our address @status - What are we doing? @nets - Associated direct netrange @next - next element in the list of interfaces


.. _`atalk_iface.definition`:

Definition
----------

.. code-block:: c

  struct atalk_iface {
    #define ATIF_PROBE	1
    #define ATIF_PROBE_FAIL	2
  };


.. _`atalk_iface.members`:

Members
-------


