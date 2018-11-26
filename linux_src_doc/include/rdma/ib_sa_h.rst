.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/rdma/ib_sa.h

.. _`sa_path_rec_roce`:

struct sa_path_rec_roce
=======================

.. c:type:: struct sa_path_rec_roce

    RoCE specific portion of the path record entry

.. _`sa_path_rec_roce.definition`:

Definition
----------

.. code-block:: c

    struct sa_path_rec_roce {
        bool route_resolved;
        u8 dmac[ETH_ALEN];
    }

.. _`sa_path_rec_roce.members`:

Members
-------

route_resolved
    When set, it indicates that this route is already
    resolved for this path record entry.

dmac
    Destination mac address for the given DGID entry
    of the path record entry.

.. _`ib_sa_register_client`:

ib_sa_register_client
=====================

.. c:function:: void ib_sa_register_client(struct ib_sa_client *client)

    Register an SA client.

    :param client:
        *undescribed*
    :type client: struct ib_sa_client \*

.. _`ib_sa_unregister_client`:

ib_sa_unregister_client
=======================

.. c:function:: void ib_sa_unregister_client(struct ib_sa_client *client)

    Deregister an SA client.

    :param client:
        Client object to deregister.
    :type client: struct ib_sa_client \*

.. _`ib_sa_join_multicast`:

ib_sa_join_multicast
====================

.. c:function:: struct ib_sa_multicast *ib_sa_join_multicast(struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct ib_sa_mcmember_rec *rec, ib_sa_comp_mask comp_mask, gfp_t gfp_mask, int (*callback)(int status, struct ib_sa_multicast *multicast), void *context)

    Initiates a join request to the specified multicast group.

    :param client:
        SA client
    :type client: struct ib_sa_client \*

    :param device:
        Device associated with the multicast group.
    :type device: struct ib_device \*

    :param port_num:
        Port on the specified device to associate with the multicast
        group.
    :type port_num: u8

    :param rec:
        SA multicast member record specifying group attributes.
    :type rec: struct ib_sa_mcmember_rec \*

    :param comp_mask:
        Component mask indicating which group attributes of \ ``rec``\  are
        valid.
    :type comp_mask: ib_sa_comp_mask

    :param gfp_mask:
        GFP mask for memory allocations.
    :type gfp_mask: gfp_t

    :param int (\*callback)(int status, struct ib_sa_multicast \*multicast):
        User callback invoked once the join operation completes.

    :param context:
        User specified context stored with the ib_sa_multicast structure.
    :type context: void \*

.. _`ib_sa_join_multicast.description`:

Description
-----------

This call initiates a multicast join request with the SA for the specified
multicast group.  If the join operation is started successfully, it returns
an ib_sa_multicast structure that is used to track the multicast operation.
Users must free this structure by calling ib_free_multicast, even if the
join operation later fails.  (The callback status is non-zero.)

If the join operation fails; status will be non-zero, with the following

.. _`ib_sa_join_multicast.failures-possible`:

failures possible
-----------------

-ETIMEDOUT: The request timed out.
-EIO: An error occurred sending the query.
-EINVAL: The MCMemberRecord values differed from the existing group's.
-ENETRESET: Indicates that an fatal error has occurred on the multicast
group, and the user must rejoin the group to continue using it.

.. _`ib_sa_free_multicast`:

ib_sa_free_multicast
====================

.. c:function:: void ib_sa_free_multicast(struct ib_sa_multicast *multicast)

    Frees the multicast tracking structure, and releases any reference on the multicast group.

    :param multicast:
        Multicast tracking structure allocated by ib_join_multicast.
    :type multicast: struct ib_sa_multicast \*

.. _`ib_sa_free_multicast.description`:

Description
-----------

This call blocks until the multicast identifier is destroyed.  It may
not be called from within the multicast callback; however, returning a non-
zero value from the callback will result in destroying the multicast
tracking structure.

.. _`ib_sa_get_mcmember_rec`:

ib_sa_get_mcmember_rec
======================

.. c:function:: int ib_sa_get_mcmember_rec(struct ib_device *device, u8 port_num, union ib_gid *mgid, struct ib_sa_mcmember_rec *rec)

    Looks up a multicast member record by its MGID and returns it if found.

    :param device:
        Device associated with the multicast group.
    :type device: struct ib_device \*

    :param port_num:
        Port on the specified device to associate with the multicast
        group.
    :type port_num: u8

    :param mgid:
        MGID of multicast group.
    :type mgid: union ib_gid \*

    :param rec:
        Location to copy SA multicast member record.
    :type rec: struct ib_sa_mcmember_rec \*

.. _`ib_init_ah_from_mcmember`:

ib_init_ah_from_mcmember
========================

.. c:function:: int ib_init_ah_from_mcmember(struct ib_device *device, u8 port_num, struct ib_sa_mcmember_rec *rec, struct net_device *ndev, enum ib_gid_type gid_type, struct rdma_ah_attr *ah_attr)

    Initialize address handle attributes based on an SA multicast member record.

    :param device:
        *undescribed*
    :type device: struct ib_device \*

    :param port_num:
        *undescribed*
    :type port_num: u8

    :param rec:
        *undescribed*
    :type rec: struct ib_sa_mcmember_rec \*

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param gid_type:
        *undescribed*
    :type gid_type: enum ib_gid_type

    :param ah_attr:
        *undescribed*
    :type ah_attr: struct rdma_ah_attr \*

.. _`ib_sa_pack_path`:

ib_sa_pack_path
===============

.. c:function:: void ib_sa_pack_path(struct sa_path_rec *rec, void *attribute)

    Conert a path record from struct ib_sa_path_rec to IB MAD wire format.

    :param rec:
        *undescribed*
    :type rec: struct sa_path_rec \*

    :param attribute:
        *undescribed*
    :type attribute: void \*

.. _`ib_sa_unpack_path`:

ib_sa_unpack_path
=================

.. c:function:: void ib_sa_unpack_path(void *attribute, struct sa_path_rec *rec)

    Convert a path record from MAD format to struct ib_sa_path_rec.

    :param attribute:
        *undescribed*
    :type attribute: void \*

    :param rec:
        *undescribed*
    :type rec: struct sa_path_rec \*

.. This file was automatic generated / don't edit.

