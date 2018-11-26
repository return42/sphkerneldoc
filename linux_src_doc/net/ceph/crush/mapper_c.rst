.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ceph/crush/mapper.c

.. _`crush_find_rule`:

crush_find_rule
===============

.. c:function:: int crush_find_rule(const struct crush_map *map, int ruleset, int type, int size)

    find a crush_rule id for a given ruleset, type, and size.

    :param map:
        the crush_map
    :type map: const struct crush_map \*

    :param ruleset:
        the storage ruleset id (user defined)
    :type ruleset: int

    :param type:
        storage ruleset type (user defined)
    :type type: int

    :param size:
        output set size
    :type size: int

.. _`crush_choose_firstn`:

crush_choose_firstn
===================

.. c:function:: int crush_choose_firstn(const struct crush_map *map, struct crush_work *work, const struct crush_bucket *bucket, const __u32 *weight, int weight_max, int x, int numrep, int type, int *out, int outpos, int out_size, unsigned int tries, unsigned int recurse_tries, unsigned int local_retries, unsigned int local_fallback_retries, int recurse_to_leaf, unsigned int vary_r, unsigned int stable, int *out2, int parent_r, const struct crush_choose_arg *choose_args)

    choose numrep distinct items of given type

    :param map:
        the crush_map
    :type map: const struct crush_map \*

    :param work:
        *undescribed*
    :type work: struct crush_work \*

    :param bucket:
        the bucket we are choose an item from
    :type bucket: const struct crush_bucket \*

    :param weight:
        *undescribed*
    :type weight: const __u32 \*

    :param weight_max:
        *undescribed*
    :type weight_max: int

    :param x:
        crush input value
    :type x: int

    :param numrep:
        the number of items to choose
    :type numrep: int

    :param type:
        the type of item to choose
    :type type: int

    :param out:
        pointer to output vector
    :type out: int \*

    :param outpos:
        our position in that vector
    :type outpos: int

    :param out_size:
        size of the out vector
    :type out_size: int

    :param tries:
        number of attempts to make
    :type tries: unsigned int

    :param recurse_tries:
        number of attempts to have recursive chooseleaf make
    :type recurse_tries: unsigned int

    :param local_retries:
        localized retries
    :type local_retries: unsigned int

    :param local_fallback_retries:
        localized fallback retries
    :type local_fallback_retries: unsigned int

    :param recurse_to_leaf:
        true if we want one device under each item of given type (chooseleaf instead of choose)
    :type recurse_to_leaf: int

    :param vary_r:
        pass r to recursive calls
    :type vary_r: unsigned int

    :param stable:
        stable mode starts rep=0 in the recursive call for all replicas
    :type stable: unsigned int

    :param out2:
        second output vector for leaf items (if \ ``recurse_to_leaf``\ )
    :type out2: int \*

    :param parent_r:
        r value passed from the parent
    :type parent_r: int

    :param choose_args:
        *undescribed*
    :type choose_args: const struct crush_choose_arg \*

.. _`crush_choose_indep`:

crush_choose_indep
==================

.. c:function:: void crush_choose_indep(const struct crush_map *map, struct crush_work *work, const struct crush_bucket *bucket, const __u32 *weight, int weight_max, int x, int left, int numrep, int type, int *out, int outpos, unsigned int tries, unsigned int recurse_tries, int recurse_to_leaf, int *out2, int parent_r, const struct crush_choose_arg *choose_args)

    alternative breadth-first positionally stable mapping

    :param map:
        *undescribed*
    :type map: const struct crush_map \*

    :param work:
        *undescribed*
    :type work: struct crush_work \*

    :param bucket:
        *undescribed*
    :type bucket: const struct crush_bucket \*

    :param weight:
        *undescribed*
    :type weight: const __u32 \*

    :param weight_max:
        *undescribed*
    :type weight_max: int

    :param x:
        *undescribed*
    :type x: int

    :param left:
        *undescribed*
    :type left: int

    :param numrep:
        *undescribed*
    :type numrep: int

    :param type:
        *undescribed*
    :type type: int

    :param out:
        *undescribed*
    :type out: int \*

    :param outpos:
        *undescribed*
    :type outpos: int

    :param tries:
        *undescribed*
    :type tries: unsigned int

    :param recurse_tries:
        *undescribed*
    :type recurse_tries: unsigned int

    :param recurse_to_leaf:
        *undescribed*
    :type recurse_to_leaf: int

    :param out2:
        *undescribed*
    :type out2: int \*

    :param parent_r:
        *undescribed*
    :type parent_r: int

    :param choose_args:
        *undescribed*
    :type choose_args: const struct crush_choose_arg \*

.. _`crush_do_rule`:

crush_do_rule
=============

.. c:function:: int crush_do_rule(const struct crush_map *map, int ruleno, int x, int *result, int result_max, const __u32 *weight, int weight_max, void *cwin, const struct crush_choose_arg *choose_args)

    calculate a mapping with the given input and rule

    :param map:
        the crush_map
    :type map: const struct crush_map \*

    :param ruleno:
        the rule id
    :type ruleno: int

    :param x:
        hash input
    :type x: int

    :param result:
        pointer to result vector
    :type result: int \*

    :param result_max:
        maximum result size
    :type result_max: int

    :param weight:
        weight vector (for map leaves)
    :type weight: const __u32 \*

    :param weight_max:
        size of weight vector
    :type weight_max: int

    :param cwin:
        pointer to at least \ :c:func:`crush_work_size`\  bytes of memory
    :type cwin: void \*

    :param choose_args:
        weights and ids for each known bucket
    :type choose_args: const struct crush_choose_arg \*

.. This file was automatic generated / don't edit.

