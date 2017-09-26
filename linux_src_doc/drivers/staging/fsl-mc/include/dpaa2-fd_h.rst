.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/dpaa2-fd.h

.. _`dpaa2-fd---frame-descriptor-apis-for-dpaa2`:

DPAA2 FD - Frame Descriptor APIs for DPAA2
==========================================

Frame Descriptors (FDs) are used to describe frame data in the DPAA2.
Frames can be enqueued and dequeued to Frame Queues (FQs) which are consumed
by the various DPAA accelerators (WRIOP, SEC, PME, DCE)

There are three types of frames: single, scatter gather, and frame lists.

The set of APIs in this file must be used to create, manipulate and
query Frame Descriptors.

.. _`dpaa2_fd`:

struct dpaa2_fd
===============

.. c:type:: struct dpaa2_fd

    Struct describing FDs

.. _`dpaa2_fd.definition`:

Definition
----------

.. code-block:: c

    struct dpaa2_fd {
        union {
            u32 words[8];
            struct dpaa2_fd_simple {
                __le64 addr;
                __le32 len;
                __le16 bpid;
                __le16 format_offset;
                __le32 frc;
                __le32 ctrl;
                __le64 flc;
            } simple;
        } ;
    }

.. _`dpaa2_fd.members`:

Members
-------

{unnamed_union}
    anonymous

words
    for easier/faster copying the whole FD structure

simple
    *undescribed*

.. _`dpaa2_fd.description`:

Description
-----------

This structure represents the basic Frame Descriptor used in the system.

.. _`dpaa2_fd_get_addr`:

dpaa2_fd_get_addr
=================

.. c:function:: dma_addr_t dpaa2_fd_get_addr(const struct dpaa2_fd *fd)

    get the addr field of frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_addr.description`:

Description
-----------

Return the address in the frame descriptor.

.. _`dpaa2_fd_set_addr`:

dpaa2_fd_set_addr
=================

.. c:function:: void dpaa2_fd_set_addr(struct dpaa2_fd *fd, dma_addr_t addr)

    Set the addr field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param dma_addr_t addr:
        the address needs to be set in frame descriptor

.. _`dpaa2_fd_get_frc`:

dpaa2_fd_get_frc
================

.. c:function:: u32 dpaa2_fd_get_frc(const struct dpaa2_fd *fd)

    Get the frame context in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_frc.description`:

Description
-----------

Return the frame context field in the frame descriptor.

.. _`dpaa2_fd_set_frc`:

dpaa2_fd_set_frc
================

.. c:function:: void dpaa2_fd_set_frc(struct dpaa2_fd *fd, u32 frc)

    Set the frame context in the frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param u32 frc:
        the frame context needs to be set in frame descriptor

.. _`dpaa2_fd_get_ctrl`:

dpaa2_fd_get_ctrl
=================

.. c:function:: u32 dpaa2_fd_get_ctrl(const struct dpaa2_fd *fd)

    Get the control bits in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_ctrl.description`:

Description
-----------

Return the control bits field in the frame descriptor.

.. _`dpaa2_fd_set_ctrl`:

dpaa2_fd_set_ctrl
=================

.. c:function:: void dpaa2_fd_set_ctrl(struct dpaa2_fd *fd, u32 ctrl)

    Set the control bits in the frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param u32 ctrl:
        the control bits to be set in the frame descriptor

.. _`dpaa2_fd_get_flc`:

dpaa2_fd_get_flc
================

.. c:function:: dma_addr_t dpaa2_fd_get_flc(const struct dpaa2_fd *fd)

    Get the flow context in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_flc.description`:

Description
-----------

Return the flow context in the frame descriptor.

.. _`dpaa2_fd_set_flc`:

dpaa2_fd_set_flc
================

.. c:function:: void dpaa2_fd_set_flc(struct dpaa2_fd *fd, dma_addr_t flc_addr)

    Set the flow context field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param dma_addr_t flc_addr:
        the flow context needs to be set in frame descriptor

.. _`dpaa2_fd_get_len`:

dpaa2_fd_get_len
================

.. c:function:: u32 dpaa2_fd_get_len(const struct dpaa2_fd *fd)

    Get the length in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_len.description`:

Description
-----------

Return the length field in the frame descriptor.

.. _`dpaa2_fd_set_len`:

dpaa2_fd_set_len
================

.. c:function:: void dpaa2_fd_set_len(struct dpaa2_fd *fd, u32 len)

    Set the length field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param u32 len:
        the length needs to be set in frame descriptor

.. _`dpaa2_fd_get_offset`:

dpaa2_fd_get_offset
===================

.. c:function:: uint16_t dpaa2_fd_get_offset(const struct dpaa2_fd *fd)

    Get the offset field in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_offset.description`:

Description
-----------

Return the offset.

.. _`dpaa2_fd_set_offset`:

dpaa2_fd_set_offset
===================

.. c:function:: void dpaa2_fd_set_offset(struct dpaa2_fd *fd, uint16_t offset)

    Set the offset field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param uint16_t offset:
        the offset needs to be set in frame descriptor

.. _`dpaa2_fd_get_format`:

dpaa2_fd_get_format
===================

.. c:function:: enum dpaa2_fd_format dpaa2_fd_get_format(const struct dpaa2_fd *fd)

    Get the format field in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_format.description`:

Description
-----------

Return the format.

.. _`dpaa2_fd_set_format`:

dpaa2_fd_set_format
===================

.. c:function:: void dpaa2_fd_set_format(struct dpaa2_fd *fd, enum dpaa2_fd_format format)

    Set the format field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param enum dpaa2_fd_format format:
        the format needs to be set in frame descriptor

.. _`dpaa2_fd_get_bpid`:

dpaa2_fd_get_bpid
=================

.. c:function:: uint16_t dpaa2_fd_get_bpid(const struct dpaa2_fd *fd)

    Get the bpid field in the frame descriptor

    :param const struct dpaa2_fd \*fd:
        the given frame descriptor

.. _`dpaa2_fd_get_bpid.description`:

Description
-----------

Return the buffer pool id.

.. _`dpaa2_fd_set_bpid`:

dpaa2_fd_set_bpid
=================

.. c:function:: void dpaa2_fd_set_bpid(struct dpaa2_fd *fd, uint16_t bpid)

    Set the bpid field of frame descriptor

    :param struct dpaa2_fd \*fd:
        the given frame descriptor

    :param uint16_t bpid:
        buffer pool id to be set

.. _`dpaa2_sg_entry`:

struct dpaa2_sg_entry
=====================

.. c:type:: struct dpaa2_sg_entry

    the scatter-gathering structure

.. _`dpaa2_sg_entry.definition`:

Definition
----------

.. code-block:: c

    struct dpaa2_sg_entry {
        __le64 addr;
        __le32 len;
        __le16 bpid;
        __le16 format_offset;
    }

.. _`dpaa2_sg_entry.members`:

Members
-------

addr
    address of the sg entry

len
    length in this sg entry

bpid
    buffer pool id

format_offset
    format and offset fields

.. _`dpaa2_sg_get_addr`:

dpaa2_sg_get_addr
=================

.. c:function:: dma_addr_t dpaa2_sg_get_addr(const struct dpaa2_sg_entry *sg)

    Get the address from SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_get_addr.description`:

Description
-----------

Return the address.

.. _`dpaa2_sg_set_addr`:

dpaa2_sg_set_addr
=================

.. c:function:: void dpaa2_sg_set_addr(struct dpaa2_sg_entry *sg, dma_addr_t addr)

    Set the address in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param dma_addr_t addr:
        the address to be set

.. _`dpaa2_sg_get_len`:

dpaa2_sg_get_len
================

.. c:function:: u32 dpaa2_sg_get_len(const struct dpaa2_sg_entry *sg)

    Get the length in SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_get_len.description`:

Description
-----------

Return the length.

.. _`dpaa2_sg_set_len`:

dpaa2_sg_set_len
================

.. c:function:: void dpaa2_sg_set_len(struct dpaa2_sg_entry *sg, u32 len)

    Set the length in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param u32 len:
        the length to be set

.. _`dpaa2_sg_get_offset`:

dpaa2_sg_get_offset
===================

.. c:function:: u16 dpaa2_sg_get_offset(const struct dpaa2_sg_entry *sg)

    Get the offset in SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_get_offset.description`:

Description
-----------

Return the offset.

.. _`dpaa2_sg_set_offset`:

dpaa2_sg_set_offset
===================

.. c:function:: void dpaa2_sg_set_offset(struct dpaa2_sg_entry *sg, u16 offset)

    Set the offset in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param u16 offset:
        the offset to be set

.. _`dpaa2_sg_get_format`:

dpaa2_sg_get_format
===================

.. c:function:: enum dpaa2_sg_format dpaa2_sg_get_format(const struct dpaa2_sg_entry *sg)

    Get the SG format in SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_get_format.description`:

Description
-----------

Return the format.

.. _`dpaa2_sg_set_format`:

dpaa2_sg_set_format
===================

.. c:function:: void dpaa2_sg_set_format(struct dpaa2_sg_entry *sg, enum dpaa2_sg_format format)

    Set the SG format in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param enum dpaa2_sg_format format:
        the format to be set

.. _`dpaa2_sg_get_bpid`:

dpaa2_sg_get_bpid
=================

.. c:function:: u16 dpaa2_sg_get_bpid(const struct dpaa2_sg_entry *sg)

    Get the buffer pool id in SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_get_bpid.description`:

Description
-----------

Return the bpid.

.. _`dpaa2_sg_set_bpid`:

dpaa2_sg_set_bpid
=================

.. c:function:: void dpaa2_sg_set_bpid(struct dpaa2_sg_entry *sg, u16 bpid)

    Set the buffer pool id in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param u16 bpid:
        the bpid to be set

.. _`dpaa2_sg_is_final`:

dpaa2_sg_is_final
=================

.. c:function:: bool dpaa2_sg_is_final(const struct dpaa2_sg_entry *sg)

    Check final bit in SG entry

    :param const struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

.. _`dpaa2_sg_is_final.description`:

Description
-----------

Return bool.

.. _`dpaa2_sg_set_final`:

dpaa2_sg_set_final
==================

.. c:function:: void dpaa2_sg_set_final(struct dpaa2_sg_entry *sg, bool final)

    Set the final bit in SG entry

    :param struct dpaa2_sg_entry \*sg:
        the given scatter-gathering object

    :param bool final:
        the final boolean to be set

.. This file was automatic generated / don't edit.

