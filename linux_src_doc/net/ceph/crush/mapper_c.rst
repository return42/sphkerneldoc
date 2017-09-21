.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ceph/crush/mapper.c

.. _`crush_find_rule`:

crush_find_rule
===============

.. c:function:: int crush_find_rule(const struct crush_map *map, int ruleset, int type, int size)

    find a crush_rule id for a given ruleset, type, and size.

    :param const struct crush_map \*map:
        the crush_map

    :param int ruleset:
        the storage ruleset id (user defined)

    :param int type:
        storage ruleset type (user defined)

    :param int size:
        output set size

.. _`crush_choose_firstn`:

crush_choose_firstn
===================

.. c:function:: int crush_choose_firstn(const struct crush_map *map, struct crush_work *work, const struct crush_bucket *bucket, const __u32 *weight, int weight_max, int x, int numrep, int type, int *out, int outpos, int out_size, unsigned int tries, unsigned int recurse_tries, unsigned int local_retries, unsigned int local_fallback_retries, int recurse_to_leaf, unsigned int vary_r, unsigned int stable, int *out2, int parent_r, const struct crush_choose_arg *choose_args)

    choose numrep distinct items of given type

    :param const struct crush_map \*map:
        the crush_map

    :param struct crush_work \*work:
        *undescribed*

    :param const struct crush_bucket \*bucket:
        the bucket we are choose an item from

    :param const __u32 \*weight:
        *undescribed*

    :param int weight_max:
        *undescribed*

    :param int x:
        crush input value

    :param int numrep:
        the number of items to choose

    :param int type:
        the type of item to choose

    :param int \*out:
        pointer to output vector

    :param int outpos:
        our position in that vector

    :param int out_size:
        size of the out vector

    :param unsigned int tries:
        number of attempts to make

    :param unsigned int recurse_tries:
        number of attempts to have recursive chooseleaf make

    :param unsigned int local_retries:
        localized retries

    :param unsigned int local_fallback_retries:
        localized fallback retries

    :param int recurse_to_leaf:
        true if we want one device under each item of given type (chooseleaf instead of choose)

    :param unsigned int vary_r:
        pass r to recursive calls

    :param unsigned int stable:
        stable mode starts rep=0 in the recursive call for all replicas

    :param int \*out2:
        second output vector for leaf items (if \ ``recurse_to_leaf``\ )

    :param int parent_r:
        r value passed from the parent

    :param const struct crush_choose_arg \*choose_args:
        *undescribed*

.. _`crush_choose_indep`:

crush_choose_indep
==================

.. c:function:: void crush_choose_indep(const struct crush_map *map, struct crush_work *work, const struct crush_bucket *bucket, const __u32 *weight, int weight_max, int x, int left, int numrep, int type, int *out, int outpos, unsigned int tries, unsigned int recurse_tries, int recurse_to_leaf, int *out2, int parent_r, const struct crush_choose_arg *choose_args)

    alternative breadth-first positionally stable mapping

    :param const struct crush_map \*map:
        *undescribed*

    :param struct crush_work \*work:
        *undescribed*

    :param const struct crush_bucket \*bucket:
        *undescribed*

    :param const __u32 \*weight:
        *undescribed*

    :param int weight_max:
        *undescribed*

    :param int x:
        *undescribed*

    :param int left:
        *undescribed*

    :param int numrep:
        *undescribed*

    :param int type:
        *undescribed*

    :param int \*out:
        *undescribed*

    :param int outpos:
        *undescribed*

    :param unsigned int tries:
        *undescribed*

    :param unsigned int recurse_tries:
        *undescribed*

    :param int recurse_to_leaf:
        *undescribed*

    :param int \*out2:
        *undescribed*

    :param int parent_r:
        *undescribed*

    :param const struct crush_choose_arg \*choose_args:
        *undescribed*

.. _`crush_do_rule`:

crush_do_rule
=============

.. c:function:: int crush_do_rule(const struct crush_map *map, int ruleno, int x, int *result, int result_max, const __u32 *weight, int weight_max, void *cwin, const struct crush_choose_arg *choose_args)

    calculate a mapping with the given input and rule

    :param const struct crush_map \*map:
        the crush_map

    :param int ruleno:
        the rule id

    :param int x:
        hash input

    :param int \*result:
        pointer to result vector

    :param int result_max:
        maximum result size

    :param const __u32 \*weight:
        weight vector (for map leaves)

    :param int weight_max:
        size of weight vector

    :param void \*cwin:
        pointer to at least \ :c:func:`crush_work_size`\  bytes of memory

    :param const struct crush_choose_arg \*choose_args:
        weights and ids for each known bucket

.. This file was automatic generated / don't edit.

