
.. _API-struct-w1-reg-num:

=================
struct w1_reg_num
=================

*man struct w1_reg_num(9)*

*4.6.0-rc1*

broken out slave device id


Synopsis
========

.. code-block:: c

    struct w1_reg_num {
    #if defined(__LITTLE_ENDIAN_BITFIELD)
      __u64 family:8;
      __u64 id:48;
      __u64 crc:8;
    #elif defined(__BIG_ENDIAN_BITFIELD)
      __u64 crc:8;
      __u64 id:48;
      __u64 family:8;
    #else
    #error "Please fix <asm/byteorder.h>"
    #endif
    };


Members
=======

family
    identifies the type of device

id
    along with family is the unique device id

crc
    checksum of the other bytes

crc
    checksum of the other bytes

id
    along with family is the unique device id

family
    identifies the type of device
