
.. _API-struct-usb-os-desc-ext-prop:

===========================
struct usb_os_desc_ext_prop
===========================

*man struct usb_os_desc_ext_prop(9)*

*4.6.0-rc1*

describes one “Extended Property”


Synopsis
========

.. code-block:: c

    struct usb_os_desc_ext_prop {
      struct list_head entry;
      u8 type;
      int name_len;
      char * name;
      int data_len;
      char * data;
      struct config_item item;
    };


Members
=======

entry
    used to keep a list of extended properties

type
    Extended Property type

name_len
    Extended Property unicode name length, including terminating '\\0'

name
    Extended Property name

data_len
    Length of Extended Property blob (for unicode store double len)

data
    Extended Property blob

item
    Represents this Extended Property in configfs
