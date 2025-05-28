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


class PropertyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def parcel(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[typing.List[params.GeoCoordinate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radius: typing.Union[
            typing.Optional[float], type_utils.NotGiven
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
        unit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyParcelResponse:
        """
        Property Boundary API

        Shape files API and property search API. All requests return the parcel boundaries
        in GEOJSON format. Quickly implement this API into your mapping applications.


        POST /v1/PropertyParcel

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            city: City name
            county: County name
            fips: FIPS county code
            house: House number
            id: Property ID
            latitude: float
            longitude: float
            polygon: typing.List[GeoCoordinate]
            radius: float
            resultIndex: int
            size: int
            state: str
            street: Street name
            unit: Unit number
            zip: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Property parcel boundaries retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.parcel()
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "apn": apn,
                "city": city,
                "county": county,
                "fips": fips,
                "house": house,
                "id": id,
                "latitude": latitude,
                "longitude": longitude,
                "polygon": polygon,
                "radius": radius,
                "result_index": result_index,
                "size": size,
                "state": state,
                "street": street,
                "unit": unit,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyParcelParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v1/PropertyParcel",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyParcelResponse,
            request_options=request_options or default_request_options(),
        )

    def comparables(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyComparablesResponse:
        """
        Property Comparables API v2

        Generate property comparables (comps) for valuation analysis using our standard algorithm.


        POST /v2/PropertyComps

        Args:
            address: Fully formatted address
            id: Property ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Property comparables retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.comparables()
        ```
        """
        _json = to_encodable(
            item={"address": address, "id": id},
            dump_with=params._SerializerPropertyCompsParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyComps",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyComparablesResponse,
            request_options=request_options or default_request_options(),
        )

    def details(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        comps: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exact_match: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyDetailsResponse:
        """
        Property Detail API

        Comprehensive property information including comps, mortgages, mailing addresses,
        property sales history & more!


        POST /v2/PropertyDetail

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            city: City name
            comps: Include comparable properties
            county: County name
            exact_match: Require exact address match
            fips: FIPS county code
            house: House number
            id: Property ID from search results
            state: Two-letter state code
            street: Street name
            unit: Unit number
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Detailed property information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.details()
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "apn": apn,
                "city": city,
                "comps": comps,
                "county": county,
                "exact_match": exact_match,
                "fips": fips,
                "house": house,
                "id": id,
                "state": state,
                "street": street,
                "unit": unit,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyDetailParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyDetail",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyDetailsResponse,
            request_options=request_options or default_request_options(),
        )

    def bulk_details(
        self,
        *,
        ids: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyBulkDetailsResponse:
        """
        Property Detail Bulk API

        For retrieving up to 1000 properties at once. Can be used standalone, but it's designed
        to work together with the Property Search API. Use this API for quickly exporting lists,
        or bulk search requests for analytics.


        POST /v2/PropertyDetailBulk

        Args:
            ids: List of property IDs (max 1000)
            request_options: Additional options to customize the HTTP request

        Returns:
            Bulk property details retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.bulk_details(ids=["string"])
        ```
        """
        _json = to_encodable(
            item={"ids": ids}, dump_with=params._SerializerPropertyBulkParameters
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyDetailBulk",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyBulkDetailsResponse,
            request_options=request_options or default_request_options(),
        )

    def pins(
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
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        obfuscate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.PropertyPinsResponse:
        """
        Mapping (Pins) API [BETA]

        Create unlimited map pins for PropTech mapping applications.
        Returns property data optimized for map display with coordinates and summary information.
        Only available on Growth+ Plans.


        POST /v2/PropertyMapping

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
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: Multi-polygon boundaries as string format
            obfuscate: Remove address and name fields
            polygon: Polygon boundary as string format
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
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property mapping data retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.pins()
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
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyPinsBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyMapping",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyPinsResponse,
            request_options=request_options or default_request_options(),
        )

    def search(
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
                typing.List[params.PropertySearchParametersMultiPolygonItem]
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
    ) -> models.PropertySearchResponse:
        """
        Property Search API

        Searchable API for list building, search counts, and advanced filtering on properties.
        You can also use this API to implement your own comparables API, or property analytics API.

        This API implements easy paging so your apps can easily manage filtered results in a results pane with paging.
        When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.


        POST /v2/PropertySearch

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
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: typing.List[PropertySearchParametersMultiPolygonItem]
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
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property search results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.search()
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
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerPropertySearchParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertySearch",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertySearchResponse,
            request_options=request_options or default_request_options(),
        )

    def comparables_advanced(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        arms_length: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exact_match: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_days_back: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_radius_miles: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_results: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_baths: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_beds: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_census_tract: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_county: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_neighborhood: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_zip: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyComparablesAdvancedResponse:
        """
        Property Comparables API v3

        Advanced property comparables API with customizable comp model parameters
        for more precise valuation analysis.


        POST /v3/PropertyComps

        Args:
            address: The fully formatted address for your subject property
            arms_length: Only include arms-length transactions
            bathrooms_boost: Boost factor for bathroom matching (1-50)
            bathrooms_max: int
            bathrooms_min: int
            bedrooms_boost: Boost factor for bedroom matching (1-50)
            bedrooms_max: int
            bedrooms_min: int
            exact_match: Enforces strictness on the address matching. No fuzzy matching.
            id: Property ID for subject property
            last_sale_price_max: int
            last_sale_price_min: int
            living_square_feet_boost: Boost factor for square footage matching (1-50)
            living_square_feet_max: int
            living_square_feet_min: int
            lot_square_feet_boost: Boost factor for lot size matching (1-50)
            lot_square_feet_max: int
            lot_square_feet_min: int
            max_days_back: Number of days back to search for recent sales comps
            max_radius_miles: Search radius for comparables
            max_results: Maximum number of comparable properties to return
            mls_listing_price_max: int
            mls_listing_price_min: int
            same_baths: Only include properties with same number of bathrooms
            same_beds: Only include properties with same number of bedrooms
            same_census_tract: Only include properties in same census tract
            same_county: Only include properties in same county
            same_neighborhood: Only include properties in same neighborhood
            same_zip: Only include properties in same zip code
            year_built_boost: Boost factor for year built matching (1-50)
            year_built_max: int
            year_built_min: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Customized property comparables retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.comparables_advanced(
            address="123 Main St, Arlington, VA 22205",
            max_days_back=180,
            max_radius_miles=1.0,
            max_results=10,
        )
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "arms_length": arms_length,
                "bathrooms_boost": bathrooms_boost,
                "bathrooms_max": bathrooms_max,
                "bathrooms_min": bathrooms_min,
                "bedrooms_boost": bedrooms_boost,
                "bedrooms_max": bedrooms_max,
                "bedrooms_min": bedrooms_min,
                "exact_match": exact_match,
                "id": id,
                "last_sale_price_max": last_sale_price_max,
                "last_sale_price_min": last_sale_price_min,
                "living_square_feet_boost": living_square_feet_boost,
                "living_square_feet_max": living_square_feet_max,
                "living_square_feet_min": living_square_feet_min,
                "lot_square_feet_boost": lot_square_feet_boost,
                "lot_square_feet_max": lot_square_feet_max,
                "lot_square_feet_min": lot_square_feet_min,
                "max_days_back": max_days_back,
                "max_radius_miles": max_radius_miles,
                "max_results": max_results,
                "mls_listing_price_max": mls_listing_price_max,
                "mls_listing_price_min": mls_listing_price_min,
                "same_baths": same_baths,
                "same_beds": same_beds,
                "same_census_tract": same_census_tract,
                "same_county": same_county,
                "same_neighborhood": same_neighborhood,
                "same_zip": same_zip,
                "year_built_boost": year_built_boost,
                "year_built_max": year_built_max,
                "year_built_min": year_built_min,
            },
            dump_with=params._SerializerPropertyComparablesAdvancedBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v3/PropertyComps",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyComparablesAdvancedResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncPropertyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def parcel(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[typing.List[params.GeoCoordinate]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        radius: typing.Union[
            typing.Optional[float], type_utils.NotGiven
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
        unit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyParcelResponse:
        """
        Property Boundary API

        Shape files API and property search API. All requests return the parcel boundaries
        in GEOJSON format. Quickly implement this API into your mapping applications.


        POST /v1/PropertyParcel

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            city: City name
            county: County name
            fips: FIPS county code
            house: House number
            id: Property ID
            latitude: float
            longitude: float
            polygon: typing.List[GeoCoordinate]
            radius: float
            resultIndex: int
            size: int
            state: str
            street: Street name
            unit: Unit number
            zip: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Property parcel boundaries retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.parcel()
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "apn": apn,
                "city": city,
                "county": county,
                "fips": fips,
                "house": house,
                "id": id,
                "latitude": latitude,
                "longitude": longitude,
                "polygon": polygon,
                "radius": radius,
                "result_index": result_index,
                "size": size,
                "state": state,
                "street": street,
                "unit": unit,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyParcelParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v1/PropertyParcel",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyParcelResponse,
            request_options=request_options or default_request_options(),
        )

    async def comparables(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyComparablesResponse:
        """
        Property Comparables API v2

        Generate property comparables (comps) for valuation analysis using our standard algorithm.


        POST /v2/PropertyComps

        Args:
            address: Fully formatted address
            id: Property ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Property comparables retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.comparables()
        ```
        """
        _json = to_encodable(
            item={"address": address, "id": id},
            dump_with=params._SerializerPropertyCompsParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyComps",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyComparablesResponse,
            request_options=request_options or default_request_options(),
        )

    async def details(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        apn: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        city: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        comps: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        county: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exact_match: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        fips: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        house: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        state: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        street: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        unit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        zip: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyDetailsResponse:
        """
        Property Detail API

        Comprehensive property information including comps, mortgages, mailing addresses,
        property sales history & more!


        POST /v2/PropertyDetail

        Args:
            address: Fully formatted address
            apn: Assessor's Parcel Number
            city: City name
            comps: Include comparable properties
            county: County name
            exact_match: Require exact address match
            fips: FIPS county code
            house: House number
            id: Property ID from search results
            state: Two-letter state code
            street: Street name
            unit: Unit number
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Detailed property information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.details()
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "apn": apn,
                "city": city,
                "comps": comps,
                "county": county,
                "exact_match": exact_match,
                "fips": fips,
                "house": house,
                "id": id,
                "state": state,
                "street": street,
                "unit": unit,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyDetailParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyDetail",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyDetailsResponse,
            request_options=request_options or default_request_options(),
        )

    async def bulk_details(
        self,
        *,
        ids: typing.List[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyBulkDetailsResponse:
        """
        Property Detail Bulk API

        For retrieving up to 1000 properties at once. Can be used standalone, but it's designed
        to work together with the Property Search API. Use this API for quickly exporting lists,
        or bulk search requests for analytics.


        POST /v2/PropertyDetailBulk

        Args:
            ids: List of property IDs (max 1000)
            request_options: Additional options to customize the HTTP request

        Returns:
            Bulk property details retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.bulk_details(ids=["string"])
        ```
        """
        _json = to_encodable(
            item={"ids": ids}, dump_with=params._SerializerPropertyBulkParameters
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyDetailBulk",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyBulkDetailsResponse,
            request_options=request_options or default_request_options(),
        )

    async def pins(
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
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        obfuscate: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        polygon: typing.Union[
            typing.Optional[str], type_utils.NotGiven
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
    ) -> models.PropertyPinsResponse:
        """
        Mapping (Pins) API [BETA]

        Create unlimited map pins for PropTech mapping applications.
        Returns property data optimized for map display with coordinates and summary information.
        Only available on Growth+ Plans.


        POST /v2/PropertyMapping

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
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: Multi-polygon boundaries as string format
            obfuscate: Remove address and name fields
            polygon: Polygon boundary as string format
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
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property mapping data retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.pins()
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
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerPropertyPinsBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyMapping",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyPinsResponse,
            request_options=request_options or default_request_options(),
        )

    async def search(
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
                typing.List[params.PropertySearchParametersMultiPolygonItem]
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
    ) -> models.PropertySearchResponse:
        """
        Property Search API

        Searchable API for list building, search counts, and advanced filtering on properties.
        You can also use this API to implement your own comparables API, or property analytics API.

        This API implements easy paging so your apps can easily manage filtered results in a results pane with paging.
        When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.


        POST /v2/PropertySearch

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
            mls_active: bool
            mls_cancelled: bool
            mls_days_on_market: IntRange
            mls_listing_price: IntRange
            mls_pending: bool
            mls_sold: bool
            multi_polygon: typing.List[PropertySearchParametersMultiPolygonItem]
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
            year_built: IntRange
            years_owned: IntRange
            zip: 5-digit ZIP code
            request_options: Additional options to customize the HTTP request

        Returns:
            Property search results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.search()
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
                "year_built": year_built,
                "years_owned": years_owned,
                "zip": zip,
            },
            dump_with=params._SerializerPropertySearchParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertySearch",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertySearchResponse,
            request_options=request_options or default_request_options(),
        )

    async def comparables_advanced(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        arms_length: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bathrooms_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        bedrooms_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        exact_match: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        last_sale_price_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        living_square_feet_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        lot_square_feet_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_days_back: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_radius_miles: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        max_results: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mls_listing_price_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_baths: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_beds: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_census_tract: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_county: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_neighborhood: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        same_zip: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_boost: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_max: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        year_built_min: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PropertyComparablesAdvancedResponse:
        """
        Property Comparables API v3

        Advanced property comparables API with customizable comp model parameters
        for more precise valuation analysis.


        POST /v3/PropertyComps

        Args:
            address: The fully formatted address for your subject property
            arms_length: Only include arms-length transactions
            bathrooms_boost: Boost factor for bathroom matching (1-50)
            bathrooms_max: int
            bathrooms_min: int
            bedrooms_boost: Boost factor for bedroom matching (1-50)
            bedrooms_max: int
            bedrooms_min: int
            exact_match: Enforces strictness on the address matching. No fuzzy matching.
            id: Property ID for subject property
            last_sale_price_max: int
            last_sale_price_min: int
            living_square_feet_boost: Boost factor for square footage matching (1-50)
            living_square_feet_max: int
            living_square_feet_min: int
            lot_square_feet_boost: Boost factor for lot size matching (1-50)
            lot_square_feet_max: int
            lot_square_feet_min: int
            max_days_back: Number of days back to search for recent sales comps
            max_radius_miles: Search radius for comparables
            max_results: Maximum number of comparable properties to return
            mls_listing_price_max: int
            mls_listing_price_min: int
            same_baths: Only include properties with same number of bathrooms
            same_beds: Only include properties with same number of bedrooms
            same_census_tract: Only include properties in same census tract
            same_county: Only include properties in same county
            same_neighborhood: Only include properties in same neighborhood
            same_zip: Only include properties in same zip code
            year_built_boost: Boost factor for year built matching (1-50)
            year_built_max: int
            year_built_min: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Customized property comparables retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.comparables_advanced(
            address="123 Main St, Arlington, VA 22205",
            max_days_back=180,
            max_radius_miles=1.0,
            max_results=10,
        )
        ```
        """
        _json = to_encodable(
            item={
                "address": address,
                "arms_length": arms_length,
                "bathrooms_boost": bathrooms_boost,
                "bathrooms_max": bathrooms_max,
                "bathrooms_min": bathrooms_min,
                "bedrooms_boost": bedrooms_boost,
                "bedrooms_max": bedrooms_max,
                "bedrooms_min": bedrooms_min,
                "exact_match": exact_match,
                "id": id,
                "last_sale_price_max": last_sale_price_max,
                "last_sale_price_min": last_sale_price_min,
                "living_square_feet_boost": living_square_feet_boost,
                "living_square_feet_max": living_square_feet_max,
                "living_square_feet_min": living_square_feet_min,
                "lot_square_feet_boost": lot_square_feet_boost,
                "lot_square_feet_max": lot_square_feet_max,
                "lot_square_feet_min": lot_square_feet_min,
                "max_days_back": max_days_back,
                "max_radius_miles": max_radius_miles,
                "max_results": max_results,
                "mls_listing_price_max": mls_listing_price_max,
                "mls_listing_price_min": mls_listing_price_min,
                "same_baths": same_baths,
                "same_beds": same_beds,
                "same_census_tract": same_census_tract,
                "same_county": same_county,
                "same_neighborhood": same_neighborhood,
                "same_zip": same_zip,
                "year_built_boost": year_built_boost,
                "year_built_max": year_built_max,
                "year_built_min": year_built_min,
            },
            dump_with=params._SerializerPropertyComparablesAdvancedBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v3/PropertyComps",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.PropertyComparablesAdvancedResponse,
            request_options=request_options or default_request_options(),
        )
