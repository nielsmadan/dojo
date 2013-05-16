package com.bank_ocr;

import static org.junit.Assert.*;

public class BankOCRTest {
    @org.junit.Test
    public void testFoo() throws Exception {
        BankOCR bankOCR = new BankOCR();

        assertEquals(bankOCR.foo(5), 25);
    }
}
