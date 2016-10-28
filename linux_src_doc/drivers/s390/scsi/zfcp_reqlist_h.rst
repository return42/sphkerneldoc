.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_reqlist.h

.. _`zfcp_reqlist`:

struct zfcp_reqlist
===================

.. c:type:: struct zfcp_reqlist

    Container for request list (reqlist)

.. _`zfcp_reqlist.definition`:

Definition
----------

.. code-block:: c

    struct zfcp_reqlist {
        spinlock_t lock;
        struct list_head buckets[ZFCP_REQ_LIST_BUCKETS];
    }

.. _`zfcp_reqlist.members`:

Members
-------

lock
    Spinlock for protecting the hash list

.. _`zfcp_reqlist_alloc`:

zfcp_reqlist_alloc
==================

.. c:function:: struct zfcp_reqlist *zfcp_reqlist_alloc( void)

    Allocate and initialize reqlist

    :param  void:
        no arguments

.. _`zfcp_reqlist_alloc.description`:

Description
-----------

Returns pointer to allocated reqlist on success, or NULL on
allocation failure.

.. _`zfcp_reqlist_isempty`:

zfcp_reqlist_isempty
====================

.. c:function:: int zfcp_reqlist_isempty(struct zfcp_reqlist *rl)

    Check whether the request list empty

    :param struct zfcp_reqlist \*rl:
        pointer to reqlist

.. _`zfcp_reqlist_isempty.return`:

Return
------

1 if list is empty, 0 if not

.. _`zfcp_reqlist_free`:

zfcp_reqlist_free
=================

.. c:function:: void zfcp_reqlist_free(struct zfcp_reqlist *rl)

    Free allocated memory for reqlist

    :param struct zfcp_reqlist \*rl:
        The reqlist where to free memory

.. _`zfcp_reqlist_find`:

zfcp_reqlist_find
=================

.. c:function:: struct zfcp_fsf_req *zfcp_reqlist_find(struct zfcp_reqlist *rl, unsigned long req_id)

    Lookup FSF request by its request id

    :param struct zfcp_reqlist \*rl:
        The reqlist where to lookup the FSF request

    :param unsigned long req_id:
        The request id to look for

.. _`zfcp_reqlist_find.description`:

Description
-----------

Returns a pointer to the FSF request with the specified request id
or NULL if there is no known FSF request with this id.

.. _`zfcp_reqlist_find_rm`:

zfcp_reqlist_find_rm
====================

.. c:function:: struct zfcp_fsf_req *zfcp_reqlist_find_rm(struct zfcp_reqlist *rl, unsigned long req_id)

    Lookup request by id and remove it from reqlist

    :param struct zfcp_reqlist \*rl:
        reqlist where to search and remove entry

    :param unsigned long req_id:
        The request id of the request to look for

.. _`zfcp_reqlist_find_rm.description`:

Description
-----------

This functions tries to find the FSF request with the specified
id and then removes it from the reqlist. The reqlist lock is held
during both steps of the operation.

.. _`zfcp_reqlist_find_rm.return`:

Return
------

Pointer to the FSF request if the request has been found,
NULL if it has not been found.

.. _`zfcp_reqlist_add`:

zfcp_reqlist_add
================

.. c:function:: void zfcp_reqlist_add(struct zfcp_reqlist *rl, struct zfcp_fsf_req *req)

    Add entry to reqlist

    :param struct zfcp_reqlist \*rl:
        reqlist where to add the entry

    :param struct zfcp_fsf_req \*req:
        The entry to add

.. _`zfcp_reqlist_add.description`:

Description
-----------

The request id always increases. As an optimization new requests
are added here with list_add_tail at the end of the bucket lists
while old requests are looked up starting at the beginning of the
lists.

.. _`zfcp_reqlist_move`:

zfcp_reqlist_move
=================

.. c:function:: void zfcp_reqlist_move(struct zfcp_reqlist *rl, struct list_head *list)

    Move all entries from reqlist to simple list

    :param struct zfcp_reqlist \*rl:
        The zfcp_reqlist where to remove all entries

    :param struct list_head \*list:
        The list where to move all entries

.. This file was automatic generated / don't edit.

