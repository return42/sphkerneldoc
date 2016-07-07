.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/dccp/feat.h

.. _`dccp_feat_entry`:

struct dccp_feat_entry
======================

.. c:type:: struct dccp_feat_entry

    Data structure to perform feature negotiation

.. _`dccp_feat_entry.definition`:

Definition
----------

.. code-block:: c

    struct dccp_feat_entry {
        dccp_feat_val val;
        enum dccp_feat_state state:8;
        u8 feat_num;
        bool needs_mandatory;
        bool needs_confirm;
        bool empty_confirm;
        bool is_local;
        struct list_head node;
    }

.. _`dccp_feat_entry.members`:

Members
-------

val
    feature's current value (SP features may have preference list)

state
    feature's current state

feat_num
    one of \ ``dccp_feature_numbers``\ 

needs_mandatory
    whether Mandatory options should be sent

needs_confirm
    whether to send a Confirm instead of a Change

empty_confirm
    whether to send an empty Confirm (depends on \ ``needs_confirm``\ )

is_local
    feature location (1) or feature-remote (0)

node
    list pointers, entries arranged in FIFO order

.. _`ccid_dependency`:

struct ccid_dependency
======================

.. c:type:: struct ccid_dependency

    Track changes resulting from choosing a CCID

.. _`ccid_dependency.definition`:

Definition
----------

.. code-block:: c

    struct ccid_dependency {
        u8 dependent_feat;
        bool is_local:1;
        bool is_mandatory:1:1;
        u8 val;
    }

.. _`ccid_dependency.members`:

Members
-------

dependent_feat
    one of \ ``dccp_feature_numbers``\ 

is_local
    local (1) or remote (0) \ ``dependent_feat``\ 

is_mandatory
    whether presence of \ ``dependent_feat``\  is mission-critical or not

val
    corresponding default value for \ ``dependent_feat``\  (u8 is sufficient here)

.. This file was automatic generated / don't edit.

