.. -*- coding: utf-8; mode: rst -*-

=======
ib_sa.h
=======


.. _`ib_sa_register_client`:

ib_sa_register_client
=====================

.. c:function:: void ib_sa_register_client (struct ib_sa_client *client)

    Register an SA client.

    :param struct ib_sa_client \*client:

        *undescribed*



.. _`ib_sa_unregister_client`:

ib_sa_unregister_client
=======================

.. c:function:: void ib_sa_unregister_client (struct ib_sa_client *client)

    Deregister an SA client.

    :param struct ib_sa_client \*client:
        Client object to deregister.



.. _`ib_sa_join_multicast`:

ib_sa_join_multicast
====================

.. c:function:: struct ib_sa_multicast *ib_sa_join_multicast (struct ib_sa_client *client, struct ib_device *device, u8 port_num, struct ib_sa_mcmember_rec *rec, ib_sa_comp_mask comp_mask, gfp_t gfp_mask, int (*callback) (int status, struct ib_sa_multicast *multicast, void *context)

    Initiates a join request to the specified multicast group.

    :param struct ib_sa_client \*client:
        SA client

    :param struct ib_device \*device:
        Device associated with the multicast group.

    :param u8 port_num:
        Port on the specified device to associate with the multicast
        group.

    :param struct ib_sa_mcmember_rec \*rec:
        SA multicast member record specifying group attributes.

    :param ib_sa_comp_mask comp_mask:
        Component mask indicating which group attributes of ``rec`` are
        valid.

    :param gfp_t gfp_mask:
        GFP mask for memory allocations.

    :param int (\*callback) (int status, struct ib_sa_multicast \*multicast):
        User callback invoked once the join operation completes.

    :param void \*context:
        User specified context stored with the ib_sa_multicast structure.



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

.. c:function:: void ib_sa_free_multicast (struct ib_sa_multicast *multicast)

    Frees the multicast tracking structure, and releases any reference on the multicast group.

    :param struct ib_sa_multicast \*multicast:
        Multicast tracking structure allocated by ib_join_multicast.



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

.. c:function:: int ib_sa_get_mcmember_rec (struct ib_device *device, u8 port_num, union ib_gid *mgid, struct ib_sa_mcmember_rec *rec)

    Looks up a multicast member record by its MGID and returns it if found.

    :param struct ib_device \*device:
        Device associated with the multicast group.

    :param u8 port_num:
        Port on the specified device to associate with the multicast
        group.

    :param union ib_gid \*mgid:
        MGID of multicast group.

    :param struct ib_sa_mcmember_rec \*rec:
        Location to copy SA multicast member record.



.. _`ib_init_ah_from_mcmember`:

ib_init_ah_from_mcmember
========================

.. c:function:: int ib_init_ah_from_mcmember (struct ib_device *device, u8 port_num, struct ib_sa_mcmember_rec *rec, struct net_device *ndev, enum ib_gid_type gid_type, struct ib_ah_attr *ah_attr)

    Initialize address handle attributes based on an SA multicast member record.

    :param struct ib_device \*device:

        *undescribed*

    :param u8 port_num:

        *undescribed*

    :param struct ib_sa_mcmember_rec \*rec:

        *undescribed*

    :param struct net_device \*ndev:

        *undescribed*

    :param enum ib_gid_type gid_type:

        *undescribed*

    :param struct ib_ah_attr \*ah_attr:

        *undescribed*



.. _`ib_init_ah_from_path`:

ib_init_ah_from_path
====================

.. c:function:: int ib_init_ah_from_path (struct ib_device *device, u8 port_num, struct ib_sa_path_rec *rec, struct ib_ah_attr *ah_attr)

    Initialize address handle attributes based on an SA path record.

    :param struct ib_device \*device:

        *undescribed*

    :param u8 port_num:

        *undescribed*

    :param struct ib_sa_path_rec \*rec:

        *undescribed*

    :param struct ib_ah_attr \*ah_attr:

        *undescribed*



.. _`ib_sa_pack_path`:

ib_sa_pack_path
===============

.. c:function:: void ib_sa_pack_path (struct ib_sa_path_rec *rec, void *attribute)

    Conert a path record from struct ib_sa_path_rec to IB MAD wire format.

    :param struct ib_sa_path_rec \*rec:

        *undescribed*

    :param void \*attribute:

        *undescribed*



.. _`ib_sa_unpack_path`:

ib_sa_unpack_path
=================

.. c:function:: void ib_sa_unpack_path (void *attribute, struct ib_sa_path_rec *rec)

    Convert a path record from MAD format to struct ib_sa_path_rec.

    :param void \*attribute:

        *undescribed*

    :param struct ib_sa_path_rec \*rec:

        *undescribed*

