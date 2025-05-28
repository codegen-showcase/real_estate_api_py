import typing
import typing_extensions

from real_estate_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from real_estate_api_py.types import models, params


class ReportingClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate_csv(
        self,
        *,
        absentee_owner: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        adjustable_rate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assumable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auction: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        basement: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        baths: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        beds: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        building_size: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cash_buyer: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        corporate_owned: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        count: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        death: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deck: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimated_equity: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flood_zone: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        foreclosure: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        free_clear: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        garage: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        high_equity: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inherited: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_date: typing.Union[
            typing.Optional[params.DateRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_size: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        map: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_cancelled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_days_on_market: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_pending: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_sold: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        multi_polygon: typing.Union[
            typing.Optional[
                typing.List[params.ReportingGenerateCsvBodyMultiPolygonItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        obfuscate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[typing.List[params.GeoCoordinate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pool: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pre_foreclosure: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        private_lender: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        property_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        property_use_code: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quit_claim: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radius: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reo: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        result_index: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summary: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_lien: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        vacant: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        webcomplete_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        years_owned: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingGenerateCsvResponse:
        """
        CSV Generator API

        Generate CSV exports of property data based on search criteria.
        Useful for bulk data exports and reporting.


        POST /v2/CSVBuilder

        Args:
            absentee_owner: bool
            address: Fully formatted address
            adjustable_rate: bool
            assumable: bool
            auction: bool
            basement: bool
            baths: IntRange
            beds: IntRange
            building_size: IntRange
            cash_buyer: bool
            city: City name
            corporate_owned: bool
            count: Return only count, not results
            county: County name
            death: bool
            deck: bool
            estimated_equity: IntRange
            file_name: Name for the generated CSV file
            flood_zone: bool
            foreclosure: bool
            free_clear: bool
            garage: bool
            high_equity: bool
            house: House number
            ids: List of property IDs to retrieve
            ids_only: Return only property IDs
            inherited: bool
            last_sale_date: DateRange
            last_sale_price: IntRange
            latitude: float
            longitude: float
            lot_size: IntRange
            map: Array of field names to include in CSV export
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: typing.List[ReportingGenerateCsvBodyMultiPolygonItem]
            obfuscate: Remove address and name fields
            polygon: typing.List[GeoCoordinate]
            pool: bool
            pre_foreclosure: bool
            private_lender: bool
            property_type: typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
            property_use_code: Property use code or array of codes
            quit_claim: bool
            radius: Search radius in miles
            reo: bool
            resultIndex: Starting index for pagination
            size: Number of results to return
            state: Two-letter state code
            street: Street name
            summary: Return aggregated summary data
            tax_lien: bool
            vacant: bool
            value: IntRange
            webcomplete_url: URL to notify when CSV generation is complete
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            CSV generation initiated successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reporting.generate_csv(
            file_name="property_export_2024",
            map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
        )
        ```
        """
        _json = to_encodable(
            item={
                "absentee_owner": absentee_owner,
                "address": address,
                "adjustable_rate": adjustable_rate,
                "assumable": assumable,
                "auction": auction,
                "basement": basement,
                "baths": baths,
                "beds": beds,
                "building_size": building_size,
                "cash_buyer": cash_buyer,
                "city": city,
                "corporate_owned": corporate_owned,
                "count": count,
                "county": county,
                "death": death,
                "deck": deck,
                "estimated_equity": estimated_equity,
                "file_name": file_name,
                "flood_zone": flood_zone,
                "foreclosure": foreclosure,
                "free_clear": free_clear,
                "garage": garage,
                "high_equity": high_equity,
                "house": house,
                "ids": ids,
                "ids_only": ids_only,
                "inherited": inherited,
                "last_sale_date": last_sale_date,
                "last_sale_price": last_sale_price,
                "latitude": latitude,
                "longitude": longitude,
                "lot_size": lot_size,
                "map": map,
                "mls_active": mls_active,
                "mls_cancelled": mls_cancelled,
                "mls_days_on_market": mls_days_on_market,
                "mls_listing_price": mls_listing_price,
                "mls_pending": mls_pending,
                "mls_sold": mls_sold,
                "multi_polygon": multi_polygon,
                "obfuscate": obfuscate,
                "polygon": polygon,
                "pool": pool,
                "pre_foreclosure": pre_foreclosure,
                "private_lender": private_lender,
                "property_type": property_type,
                "property_use_code": property_use_code,
                "quit_claim": quit_claim,
                "radius": radius,
                "reo": reo,
                "result_index": result_index,
                "size": size,
                "state": state,
                "street": street,
                "summary": summary,
                "tax_lien": tax_lien,
                "vacant": vacant,
                "value": value,
                "webcomplete_url": webcomplete_url,
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerReportingGenerateCsvBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/CSVBuilder",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.ReportingGenerateCsvResponse,
            request_options=request_options or default_request_options(),
        )

    def lien(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingLienResponse:
        """
        Involuntary Liens API

        Go beyond standard tax liens and add involuntary lien data to your property insights.
        Includes federal tax liens, judgment liens, mechanic's liens, and other encumbrances.


        POST /v2/Reports/PropertyLiens

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            fips: FIPS county code
            id: Property ID from search results
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property lien information retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reporting.lien(address="123 Main St, Arlington, VA 22205")
        ```
        """
        _json = to_encodable(
            item={"address": address, "apn": apn, "fips": fips, "id": id, "zip": zip},
            dump_with=params._SerializerReportingLienBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/Reports/PropertyLiens",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.ReportingLienResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncReportingClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate_csv(
        self,
        *,
        absentee_owner: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        adjustable_rate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        assumable: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        auction: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        basement: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        baths: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        beds: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        building_size: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        cash_buyer: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        corporate_owned: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        count: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        death: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        deck: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        estimated_equity: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        file_name: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        flood_zone: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        foreclosure: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        free_clear: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        garage: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        high_equity: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        ids_only: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        inherited: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_date: typing.Union[
            typing.Optional[params.DateRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_size: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        map: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_active: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_cancelled: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_days_on_market: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_pending: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_sold: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        multi_polygon: typing.Union[
            typing.Optional[
                typing.List[params.ReportingGenerateCsvBodyMultiPolygonItem]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        obfuscate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[typing.List[params.GeoCoordinate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pool: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        pre_foreclosure: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        private_lender: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        property_type: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        property_use_code: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        quit_claim: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radius: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        reo: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        result_index: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        summary: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        tax_lien: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        vacant: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        value: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        webcomplete_url: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        years_owned: typing.Union[
            typing.Optional[params.IntRange], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingGenerateCsvResponse:
        """
        CSV Generator API

        Generate CSV exports of property data based on search criteria.
        Useful for bulk data exports and reporting.


        POST /v2/CSVBuilder

        Args:
            absentee_owner: bool
            address: Fully formatted address
            adjustable_rate: bool
            assumable: bool
            auction: bool
            basement: bool
            baths: IntRange
            beds: IntRange
            building_size: IntRange
            cash_buyer: bool
            city: City name
            corporate_owned: bool
            count: Return only count, not results
            county: County name
            death: bool
            deck: bool
            estimated_equity: IntRange
            file_name: Name for the generated CSV file
            flood_zone: bool
            foreclosure: bool
            free_clear: bool
            garage: bool
            high_equity: bool
            house: House number
            ids: List of property IDs to retrieve
            ids_only: Return only property IDs
            inherited: bool
            last_sale_date: DateRange
            last_sale_price: IntRange
            latitude: float
            longitude: float
            lot_size: IntRange
            map: Array of field names to include in CSV export
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: typing.List[ReportingGenerateCsvBodyMultiPolygonItem]
            obfuscate: Remove address and name fields
            polygon: typing.List[GeoCoordinate]
            pool: bool
            pre_foreclosure: bool
            private_lender: bool
            property_type: typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
            property_use_code: Property use code or array of codes
            quit_claim: bool
            radius: Search radius in miles
            reo: bool
            resultIndex: Starting index for pagination
            size: Number of results to return
            state: Two-letter state code
            street: Street name
            summary: Return aggregated summary data
            tax_lien: bool
            vacant: bool
            value: IntRange
            webcomplete_url: URL to notify when CSV generation is complete
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            CSV generation initiated successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reporting.generate_csv(
            file_name="property_export_2024",
            map=["id", "address", "estimatedValue", "bedrooms", "bathrooms"],
        )
        ```
        """
        _json = to_encodable(
            item={
                "absentee_owner": absentee_owner,
                "address": address,
                "adjustable_rate": adjustable_rate,
                "assumable": assumable,
                "auction": auction,
                "basement": basement,
                "baths": baths,
                "beds": beds,
                "building_size": building_size,
                "cash_buyer": cash_buyer,
                "city": city,
                "corporate_owned": corporate_owned,
                "count": count,
                "county": county,
                "death": death,
                "deck": deck,
                "estimated_equity": estimated_equity,
                "file_name": file_name,
                "flood_zone": flood_zone,
                "foreclosure": foreclosure,
                "free_clear": free_clear,
                "garage": garage,
                "high_equity": high_equity,
                "house": house,
                "ids": ids,
                "ids_only": ids_only,
                "inherited": inherited,
                "last_sale_date": last_sale_date,
                "last_sale_price": last_sale_price,
                "latitude": latitude,
                "longitude": longitude,
                "lot_size": lot_size,
                "map": map,
                "mls_active": mls_active,
                "mls_cancelled": mls_cancelled,
                "mls_days_on_market": mls_days_on_market,
                "mls_listing_price": mls_listing_price,
                "mls_pending": mls_pending,
                "mls_sold": mls_sold,
                "multi_polygon": multi_polygon,
                "obfuscate": obfuscate,
                "polygon": polygon,
                "pool": pool,
                "pre_foreclosure": pre_foreclosure,
                "private_lender": private_lender,
                "property_type": property_type,
                "property_use_code": property_use_code,
                "quit_claim": quit_claim,
                "radius": radius,
                "reo": reo,
                "result_index": result_index,
                "size": size,
                "state": state,
                "street": street,
                "summary": summary,
                "tax_lien": tax_lien,
                "vacant": vacant,
                "value": value,
                "webcomplete_url": webcomplete_url,
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerReportingGenerateCsvBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/CSVBuilder",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.ReportingGenerateCsvResponse,
            request_options=request_options or default_request_options(),
        )

    async def lien(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.ReportingLienResponse:
        """
        Involuntary Liens API

        Go beyond standard tax liens and add involuntary lien data to your property insights.
        Includes federal tax liens, judgment liens, mechanic's liens, and other encumbrances.


        POST /v2/Reports/PropertyLiens

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            fips: FIPS county code
            id: Property ID from search results
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property lien information retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reporting.lien(address="123 Main St, Arlington, VA 22205")
        ```
        """
        _json = to_encodable(
            item={"address": address, "apn": apn, "fips": fips, "id": id, "zip": zip},
            dump_with=params._SerializerReportingLienBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/Reports/PropertyLiens",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.ReportingLienResponse,
            request_options=request_options or default_request_options(),
        )
