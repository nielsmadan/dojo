package com.bank_ocr;

import java.util.Arrays;

import static org.junit.Assert.*;

/**
 * Created with IntelliJ IDEA.
 * User: nielsm
 * Date: 5/29/13
 * Time: 1:06 PM
 * To change this template use File | Settings | File Templates.
 */
public class BankOCRReaderTest {
    @org.junit.Test
    public void testGetDigitParsesOne() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals("1", bankOCRReader.getDigit("  |  |  |"));
    }

    @org.junit.Test
    public void testGetDigitParsesTwo() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals("2", bankOCRReader.getDigit(" _  _||_ "));
    }

    @org.junit.Test
    public void testGetDigitParsesBad() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals("?", bankOCRReader.getDigit(" _  _||  "));
    }

    @org.junit.Test
    public void testChunkSingle() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(bankOCRReader.chunkNumberString("111222\n333444\n555666"), Arrays.asList("111333555", "222444666"));
    }

    @org.junit.Test
    public void testConvertToNumberSingleDigit() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(bankOCRReader.convertToNumber(" _ \n _|\n|_ "), "2");
    }


    @org.junit.Test
    public void testConvertToNumberMultipleDigit() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(bankOCRReader.convertToNumber(" _   |\n _|  |\n|_   |"), "21");
    }

    @org.junit.Test
    public void testSplitNumber() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(Arrays.asList(bankOCRReader.splitNumber("111\n222\n333\n\n444\n555\n666")), Arrays.asList("111\n222\n333", "444\n555\n666"));
    }

    @org.junit.Test
    public void testConvertNumbersSingleNumber() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(bankOCRReader.convertToNumbers(" _   |\n _|  |\n|_   |"), Arrays.asList("21"));
    }

    @org.junit.Test
    public void testConvertNumbersMultipleNumber() throws Exception {
        BankOCRReader bankOCRReader = new BankOCRReader();
        assertEquals(bankOCRReader.convertToNumbers(" _   |\n _|  |\n|_   |\n\n  |  |\n  |  |\n  |  |"), Arrays.asList("21", "11"));
    }
}
