import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {State, StateRelations, TrayMovement} from '../models';
import {TrayMovementRepository} from './tray-movement.repository';

export class StateRepository extends DefaultCrudRepository<
  State,
  typeof State.prototype.state_id,
  StateRelations
> {

  public readonly trayMovements: HasManyRepositoryFactory<TrayMovement, typeof State.prototype.state_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('TrayMovementRepository') protected trayMovementRepositoryGetter: Getter<TrayMovementRepository>,
  ) {
    super(State, dataSource);
    this.trayMovements = this.createHasManyRepositoryFactoryFor('trayMovements', trayMovementRepositoryGetter,);
    this.registerInclusionResolver('trayMovements', this.trayMovements.inclusionResolver);
  }
}
