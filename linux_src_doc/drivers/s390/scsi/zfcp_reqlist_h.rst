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

buckets
    *undescribed*

.. _`zfcp_reqlist_alloc`:

zfcp_reqlist_alloc
==================

.. c:function:: struct zfcp_reqlist *zfcp_reqlist_alloc( void)

    Allocate and initialize reqlist

    :param void:
        no arguments
    :type void: 

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

    :param rl:
        pointer to reqlist
    :type rl: struct zfcp_reqlist \*

.. _`zfcp_reqlist_isempty.return`:

Return
------

1 if list is empty, 0 if not

.. _`zfcp_reqlist_free`:

zfcp_reqlist_free
=================

.. c:function:: void zfcp_reqlist_free(struct zfcp_reqlist *rl)

    Free allocated memory for reqlist

    :param rl:
        The reqlist where to free memory
    :type rl: struct zfcp_reqlist \*

.. _`zfcp_reqlist_find`:

zfcp_reqlist_find
=================

.. c:function:: struct zfcp_fsf_req *zfcp_reqlist_find(struct zfcp_reqlist *rl, unsigned long req_id)

    Lookup FSF request by its request id

    :param rl:
        The reqlist where to lookup the FSF request
    :type rl: struct zfcp_reqlist \*

    :param req_id:
        The request id to look for
    :type req_id: unsigned long

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

    :param rl:
        reqlist where to search and remove entry
    :type rl: struct zfcp_reqlist \*

    :param req_id:
        The request id of the request to look for
    :type req_id: unsigned long

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

    :param rl:
        reqlist where to add the entry
    :type rl: struct zfcp_reqlist \*

    :param req:
        The entry to add
    :type req: struct zfcp_fsf_req \*

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

    :param rl:
        The zfcp_reqlist where to remove all entries
    :type rl: struct zfcp_reqlist \*

    :param list:
        The list where to move all entries
    :type list: struct list_head \*

.. _`zfcp_reqlist_apply_for_all`:

zfcp_reqlist_apply_for_all
==========================

.. c:function:: void zfcp_reqlist_apply_for_all(struct zfcp_reqlist *rl, void (*f)(struct zfcp_fsf_req *, void *), void *data)

    apply a function to every request.

    :param rl:
        the requestlist that contains the target requests.
    :type rl: struct zfcp_reqlist \*

    :param void (\*f)(struct zfcp_fsf_req \*, void \*):
        the function to apply to each request; the first parameter of the
        function will be the target-request; the second parameter is the same
        pointer as given with the argument \ ``data``\ .

    :param data:
        freely chosen argument; passed through to \ ``f``\  as second parameter.
    :type data: void \*

.. _`zfcp_reqlist_apply_for_all.description`:

Description
-----------

Uses :c:macro:\`list_for_each_entry\` to iterate over the lists in the hash-
table (not a 'safe' variant, so don't modify the list).

Holds \ ``rl->lock``\  over the entire request-iteration.

.. This file was automatic generated / don't edit.

