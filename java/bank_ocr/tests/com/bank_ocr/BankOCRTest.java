package com.bank_ocr;

import java.util.Arrays;

import static org.junit.Assert.*;

public class BankOCRTest {
    @org.junit.Test
    public void testIsValidAccountNumberTrue() throws Exception {
        BankOCR bankOCR = new BankOCR();
        assertTrue(bankOCR.isValidAccountNumberChecksum("345882865"));
    }

    @org.junit.Test
    public void testIsValidAccountNumberFalse() throws Exception {
        BankOCR bankOCR = new BankOCR();
        assertFalse(bankOCR.isValidAccountNumberChecksum("345882866"));
    }

    @org.junit.Test(expected=NumberFormatException.class)
    public void testIsValidAccountNumberInvalid() throws Exception {
        BankOCR bankOCR = new BankOCR();
        assertFalse(bankOCR.isValidAccountNumberChecksum("3458?2866"));
    }

    @org.junit.Test
    public void testIsLegibleAccountNumberTrue() {
        BankOCR bankOCR = new BankOCR();
        assertTrue(bankOCR.isLegibleAccountNumber("345882836"));
    }

    @org.junit.Test
    public void testGetNumberResultOutput() throws Exception {
        BankOCR bankOCR = new BankOCR();
        assertEquals("345882865", bankOCR.getNumberResultOutput("345882865"));
    }

    @org.junit.Test
    public void testGetNumberResultOutputWithErr() {
        BankOCR bankOCR = new BankOCR();
        assertEquals("345882866 ERR", bankOCR.getNumberResultOutput("345882866"));
    }

    @org.junit.Test
    public void testGetNumberResultOutputIllegible() {
        BankOCR bankOCR = new BankOCR();
        assertEquals("34588?866 ILL", bankOCR.getNumberResultOutput("34588?866"));
    }

    @org.junit.Test
    public void testIsLegibleAccountNumberFalse() {
        BankOCR bankOCR = new BankOCR();
        assertFalse(bankOCR.isLegibleAccountNumber("3458828?6"));
    }

    @org.junit.Test
    public void testGetNumberListValidationOutput() {
        BankOCR bankOCR = new BankOCR();
        assertEquals(Arrays.asList("345882865", "345882866 ERR", "34588?866 ILL"),
                     bankOCR.getNumberListValidationOutput(Arrays.asList("345882865", "345882866", "34588?866")));
    }
}
