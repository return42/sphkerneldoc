.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/dvb/ca.h

.. _`ca_slot_info`:

struct ca_slot_info
===================

.. c:type:: struct ca_slot_info

    CA slot interface types and info.

.. _`ca_slot_info.definition`:

Definition
----------

.. code-block:: c

    struct ca_slot_info {
        int num;
        int type;
    #define CA_CI 1
    #define CA_CI_LINK 2
    #define CA_CI_PHYS 4
    #define CA_DESCR 8
    #define CA_SC 128
        unsigned int flags;
    #define CA_CI_MODULE_PRESENT 1
    #define CA_CI_MODULE_READY 2
    }

.. _`ca_slot_info.members`:

Members
-------

num
    slot number.

type
    *undescribed*

flags
    *undescribed*

.. _`ca_slot_info.description`:

Description
-----------

This struct stores the CA slot information.

     - \ ``CA_CI``\  - CI high level interface;
     - \ ``CA_CI_LINK``\  - CI link layer level interface;
     - \ ``CA_CI_PHYS``\  - CI physical layer level interface;
     - \ ``CA_DESCR``\  - built-in descrambler;
     - \ ``CA_SC``\  -simple smart card interface.

     - \ ``CA_CI_MODULE_PRESENT``\  - module (or card) inserted;
     - \ ``CA_CI_MODULE_READY``\  - module is ready for usage.

.. _`ca_descr_info`:

struct ca_descr_info
====================

.. c:type:: struct ca_descr_info

    descrambler types and info.

.. _`ca_descr_info.definition`:

Definition
----------

.. code-block:: c

    struct ca_descr_info {
        unsigned int num;
        unsigned int type;
    #define CA_ECD 1
    #define CA_NDS 2
    #define CA_DSS 4
    }

.. _`ca_descr_info.members`:

Members
-------

num
    number of available descramblers (keys).

type
    *undescribed*

.. _`ca_descr_info.description`:

Description
-----------

Identifies the number of descramblers and their type.

     - \ ``CA_ECD``\  - European Common Descrambler (ECD) hardware;
     - \ ``CA_NDS``\  - Videoguard (NDS) hardware;
     - \ ``CA_DSS``\  - Distributed Sample Scrambling (DSS) hardware.

.. _`ca_caps`:

struct ca_caps
==============

.. c:type:: struct ca_caps

    CA slot interface capabilities.

.. _`ca_caps.definition`:

Definition
----------

.. code-block:: c

    struct ca_caps {
        unsigned int slot_num;
        unsigned int slot_type;
        unsigned int descr_num;
        unsigned int descr_type;
    }

.. _`ca_caps.members`:

Members
-------

slot_num
    total number of CA card and module slots.

slot_type
    bitmap with all supported types as defined at
    \ :c:type:`struct ca_slot_info <ca_slot_info>`\  (e. g. \ ``CA_CI``\ , \ ``CA_CI_LINK``\ , etc).

descr_num
    total number of descrambler slots (keys)

descr_type
    bitmap with all supported types as defined at
    \ :c:type:`struct ca_descr_info <ca_descr_info>`\  (e. g. \ ``CA_ECD``\ , \ ``CA_NDS``\ , etc).

.. _`ca_msg`:

struct ca_msg
=============

.. c:type:: struct ca_msg

    a message to/from a CI-CAM

.. _`ca_msg.definition`:

Definition
----------

.. code-block:: c

    struct ca_msg {
        unsigned int index;
        unsigned int type;
        unsigned int length;
        unsigned char msg[256];
    }

.. _`ca_msg.members`:

Members
-------

index
    unused

type
    unused

length
    length of the message

msg
    message

.. _`ca_msg.description`:

Description
-----------

This struct carries a message to be send/received from a CI CA module.

.. _`ca_descr`:

struct ca_descr
===============

.. c:type:: struct ca_descr

    CA descrambler control words info

.. _`ca_descr.definition`:

Definition
----------

.. code-block:: c

    struct ca_descr {
        unsigned int index;
        unsigned int parity;
        unsigned char cw[8];
    }

.. _`ca_descr.members`:

Members
-------

index
    CA Descrambler slot

parity
    control words parity, where 0 means even and 1 means odd

cw
    CA Descrambler control words

.. This file was automatic generated / don't edit.

