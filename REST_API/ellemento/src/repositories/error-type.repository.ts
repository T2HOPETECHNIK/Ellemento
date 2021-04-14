import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {ErrorType, ErrorTypeRelations} from '../models';

export class ErrorTypeRepository extends DefaultCrudRepository<
  ErrorType,
  typeof ErrorType.prototype.error_type_id,
  ErrorTypeRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(ErrorType, dataSource);
  }
}
