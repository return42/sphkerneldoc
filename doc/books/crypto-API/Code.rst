.. -*- coding: utf-8; mode: rst -*-

.. _Code:

=============
Code Examples
=============


Code Example For Symmetric Key Cipher Operation
===============================================


.. code-block:: c

    struct tcrypt_result {
        struct completion completion;
        int err;
    };

    /* tie all data structures together */
    struct skcipher_def {
        struct scatterlist sg;
        struct crypto_skcipher *tfm;
        struct skcipher_request *req;
        struct tcrypt_result result;
    };

    /* Callback function */
    static void test_skcipher_cb(struct crypto_async_request *req, int error)
    {
        struct tcrypt_result *result = req->data;

        if (error == -EINPROGRESS)
            return;
        result->err = error;
        complete(&result->completion);
        pr_info("Encryption finished successfullyn");
    }

    /* Perform cipher operation */
    static unsigned int test_skcipher_encdec(struct skcipher_def *sk,
                         int enc)
    {
        int rc = 0;

        if (enc)
            rc = crypto_skcipher_encrypt(sk->req);
        else
            rc = crypto_skcipher_decrypt(sk->req);

        switch (rc) {
        case 0:
            break;
        case -EINPROGRESS:
        case -EBUSY:
            rc = wait_for_completion_interruptible(
                &sk->result.completion);
            if (!rc && !sk->result.err) {
                reinit_completion(&sk->result.completion);
                break;
            }
        default:
            pr_info("skcipher encrypt returned with %d result %dn",
                rc, sk->result.err);
            break;
        }
        init_completion(&sk->result.completion);

        return rc;
    }

    /* Initialize and trigger cipher operation */
    static int test_skcipher(void)
    {
        struct skcipher_def sk;
        struct crypto_skcipher *skcipher = NULL;
        struct skcipher_request *req = NULL;
        char *scratchpad = NULL;
        char *ivdata = NULL;
        unsigned char key[32];
        int ret = -EFAULT;

        skcipher = crypto_alloc_skcipher("cbc-aes-aesni", 0, 0);
        if (IS_ERR(skcipher)) {
            pr_info("could not allocate skcipher handlen");
            return PTR_ERR(skcipher);
        }

        req = skcipher_request_alloc(skcipher, GFP_KERNEL);
        if (!req) {
            pr_info("could not allocate skcipher requestn");
            ret = -ENOMEM;
            goto out;
        }

        skcipher_request_set_callback(req, CRYPTO_TFM_REQ_MAY_BACKLOG,
                          test_skcipher_cb,
                          &sk.result);

        /* AES 256 with random key */
        get_random_bytes(&key, 32);
        if (crypto_skcipher_setkey(skcipher, key, 32)) {
            pr_info("key could not be setn");
            ret = -EAGAIN;
            goto out;
        }

        /* IV will be random */
        ivdata = kmalloc(16, GFP_KERNEL);
        if (!ivdata) {
            pr_info("could not allocate ivdatan");
            goto out;
        }
        get_random_bytes(ivdata, 16);

        /* Input data will be random */
        scratchpad = kmalloc(16, GFP_KERNEL);
        if (!scratchpad) {
            pr_info("could not allocate scratchpadn");
            goto out;
        }
        get_random_bytes(scratchpad, 16);

        sk.tfm = skcipher;
        sk.req = req;

        /* We encrypt one block */
        sg_init_one(&sk.sg, scratchpad, 16);
        skcipher_request_set_crypt(req, &sk.sg, &sk.sg, 16, ivdata);
        init_completion(&sk.result.completion);

        /* encrypt data */
        ret = test_skcipher_encdec(&sk, 1);
        if (ret)
            goto out;

        pr_info("Encryption triggered successfullyn");

    out:
        if (skcipher)
            crypto_free_skcipher(skcipher);
        if (req)
            skcipher_request_free(req);
        if (ivdata)
            kfree(ivdata);
        if (scratchpad)
            kfree(scratchpad);
        return ret;
    }


Code Example For Use of Operational State Memory With SHASH
===========================================================


.. code-block:: c

    struct sdesc {
        struct shash_desc shash;
        char ctx[];
    };

    static struct sdescinit_sdesc(struct crypto_shash *alg)
    {
        struct sdescsdesc;
        int size;

        size = sizeof(struct shash_desc) + crypto_shash_descsize(alg);
        sdesc = kmalloc(size, GFP_KERNEL);
        if (!sdesc)
            return ERR_PTR(-ENOMEM);
        sdesc->shash.tfm = alg;
        sdesc->shash.flags = 0x0;
        return sdesc;
    }

    static int calc_hash(struct crypto_shashalg,
                 const unsigned chardata, unsigned int datalen,
                 unsigned chardigest) {
        struct sdescsdesc;
        int ret;

        sdesc = init_sdesc(alg);
        if (IS_ERR(sdesc)) {
            pr_info("trusted_key: can't alloc %sn", hash_alg);
            return PTR_ERR(sdesc);
        }

        ret = crypto_shash_digest(&sdesc->shash, data, datalen, digest);
        kfree(sdesc);
        return ret;
    }


Code Example For Random Number Generator Usage
==============================================


.. code-block:: c

    static int get_random_numbers(u8 *buf, unsigned int len)
    {
        struct crypto_rngrng = NULL;
        chardrbg = "drbg_nopr_sha256"; /* Hash DRBG with SHA-256, no PR */
        int ret;

        if (!buf || !len) {
            pr_debug("No output buffer providedn");
            return -EINVAL;
        }

        rng = crypto_alloc_rng(drbg, 0, 0);
        if (IS_ERR(rng)) {
            pr_debug("could not allocate RNG handle for %sn", drbg);
            return -PTR_ERR(rng);
        }

        ret = crypto_rng_get_bytes(rng, buf, len);
        if (ret < 0)
            pr_debug("generation of random numbers failedn");
        else if (ret == 0)
            pr_debug("RNG returned no data");
        else
            pr_debug("RNG returned %d bytes of datan", ret);

    out:
        crypto_free_rng(rng);
        return ret;
    }




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
